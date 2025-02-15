#!/bin/bash -l

#SBATCH -p batch -N 1
#SBATCH --job-name af-run
echo $MAMBA_EXE $MAMBA_ROOT_PREFIX Hello
micromamba run -n qc python ./af-myqlm.py
micromamba run -n qc python ./classical.py

