#!/bin/bash
#
#SBATCH --job-name=test
#SBATCH --output=output.txt
#
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=15
#SBATCH --time=24:00:00
#SBATCH --mem-per-cpu=30720
#SBATCH --partition=q16

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

python3 clusterTest.py

date
hostname
sleep 300
hostname