#!/bin/bash -l
#SBATCH -p debug -N 4
#SBATCH --job-name hybrid-run-mpi

micromamba activate qc

# ~/bin/micromamba run -n qc srun -n 2 python ./quantum-task.py
srun -n 2 python ./quantum-task.py




