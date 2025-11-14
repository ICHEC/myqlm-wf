#!/bin/bash -l

#SBATCH -p cpu -N 2
#SBATCH --job-name hybrid-run-mpi
srun -n 1 python ./run_workflow.py

