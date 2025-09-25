from qlmaas.qpus import AnalogQPU
from qat.core import Variable, Observable, Schedule, Term
 
t_variable = Variable("t")
schedule = Schedule(drive=(1 - t_variable) * Observable(1, pauli_terms=[Term(1, 'Z', [0])]),
                    tmax=2.0)
 
# To simply sample the final state in the computational basis
job = schedule.to_job()
 
my_qpu = AnalogQPU()
async_result = my_qpu.submit(job)
result = async_result.join()
print(result)
