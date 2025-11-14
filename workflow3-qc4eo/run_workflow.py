from mpi4py import MPI

# spawn a process via MPI to do the classical preprocessing
worker = MPI.COMM_SELF.Spawn('python', './classical_task.py', 1)

qbits0 = worker.recv(source=0, tag=0)
print("Qubit Geometry:")
print(qbits0)

end = worker.recv(source=0, tag=1)
print("Master end signal received, end the job!")

# disconnect from worker
worker.Disconnect()


worker = MPI.COMM_SELF.Spawn('python', './quantum_task.py', 1)
worker.send(qbits0, dest=0, tag=2)

probs = worker.recv(source=0, tag=3)
print("Probabilities:")
print(probs)

end = worker.recv(source=0, tag=4)
print("Master end signal received, end the job!")

# disconnect from worker
worker.Disconnect()
