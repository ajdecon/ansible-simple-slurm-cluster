#!/bin/bash
#SBATCH -n8
module load openmpi-1.8-x86_64
mpirun -np 8 /home/rightscale/hello.py
