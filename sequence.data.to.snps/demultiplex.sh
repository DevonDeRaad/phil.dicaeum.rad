#!/bin/sh
#
#SBATCH --job-name=process.radtags            # Job Name
#SBATCH --nodes=1              # 40 nodes
#SBATCH --ntasks-per-node=1             # 40 CPU allocation per Task
#SBATCH --partition=sixhour            # Name of the Slurm partition used
#SBATCH --chdir=/home/d669d153/scratch/phil.dicaeum1/      # Set working d$
#SBATCH --mem-per-cpu=5gb            # memory requested
#SBATCH --time=360

#/home/d669d153/work/stacks-2.3b/process_radtags -p /home/d669d153/scratch/phil.dicaeum1/plate1  -o /home/d669d153/scratch/phil.dicaeum1/fastq -b plate1.barcodes.txt -e ndeI -r -c -q

/home/d669d153/work/stacks-2.3b/process_radtags -p /home/d669d153/scratch/phil.dicaeum1/plate2  -o /home/d669d153/scratch/phil.dicaeum1/fastq -b plate2.barcodes.txt -e ndeI -r -c -q
