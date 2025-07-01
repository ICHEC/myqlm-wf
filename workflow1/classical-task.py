#!/usr/bin/env python
from mpi4py import MPI
import numpy as np
from time import time
import pickle
import struc_fac as sf

#L1, L2, statevector = pickle.load(open('quantum-data.pkl', 'rb'))

# initialize MPI
comm = MPI.Comm.Get_parent()
size = comm.Get_size()
rank = comm.Get_rank()

L1 = comm.recv(source=0, tag=99)
L2 = comm.recv(source=0, tag=98)
statevector = comm.recv(source=0, tag=97)

N = L1 * L2
hsize = 2**N
ibasis = sf.get_basis(hsize=hsize, N=N)
print(f'worker Read L1, L2 = ({L1}, {L2})')

t1 = time()
s_i = sf.get_spins(statevector, ibasis, N)
t2 = time()

print(f"worker Time in s_i compute = {t2 - t1}")
np.savetxt('final-si.dat', s_i)

t1 = time()
s_ij = sf.get_sisj(statevector, ibasis, N)
t2 = time()

pickle.dump(s_ij, open('classical-data.pkl', 'wb'))
print(f"worker Time in s_ij compute = {t2 - t1}")

comm.send(1, dest=0, tag=88)
comm.Disconnect()
