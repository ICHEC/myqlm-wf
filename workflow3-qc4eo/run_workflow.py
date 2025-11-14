from mpi4py import MPI

# spawn a process via MPI to do the classical preprocessing
worker = MPI.COMM_SELF.Spawn('python', './classical_task.py', 1)

qbits0 = worker.recv(source=0, tag=99)

print(qbits0)

end = worker.recv(source=0, tag=88)
print("Master end signal received, end the job!")

# disconnect from worker
worker.Disconnect()

