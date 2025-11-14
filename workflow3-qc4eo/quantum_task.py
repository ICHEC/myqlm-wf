from qlmaas.qpus import AnalogQPU
from qat.core import Observable, Schedule, Term

import numpy as np
from mpi4py import MPI


c6 = 865723.02  # (rad/µs)(µm)**6
duration = 660 # ns
amplitude = 2*np.pi # rad/µs

def occ_op(nqbits, qi):
    return (1 - Observable(nqbits, pauli_terms=[Term(1.0, "Z", [qi])])) / 2


def generate_rydberg_hamiltonian(qbits):
    nqbits = len(qbits)
    
    amplitude_term = Observable(nqbits, pauli_terms=[Term(0.5, "X", [i]) for i in range(nqbits)])

    interaction_term = 0
    for i in range(nqbits-1):
        for j in range(i + 1, nqbits):
            rij = np.linalg.norm(qbits[i] - qbits[j])
            interaction_term += (
                (1 / rij ** 6)
                * occ_op(nqbits, i)
                * occ_op(nqbits, j)
            )

    return [
        (amplitude, amplitude_term),
        (c6, interaction_term),
    ]


comm = MPI.Comm.Get_parent()

qubit_coords = comm.recv(source=0, tag=2)

schedule = Schedule(drive=generate_rydberg_hamiltonian(qubit_coords),
            tmax=duration/1000)

job = schedule.to_job()

my_qpu = AnalogQPU()
async_result = my_qpu.submit(job)
result = async_result.join()

probs = np.array([r.probability for r in result])
comm.send(probs, dest=0, tag=3)

comm.send(1, dest=0, tag=4)
comm.Disconnect()
