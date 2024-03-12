#!/bin/sh
#
#SBATCH --job-name=phylonet             # Job Name
#SBATCH --nodes=1             # 40 nodes
#SBATCH --ntasks-per-node=15               # 40 CPU allocation per Task
#SBATCH --partition=bi            # Name of the Slurm partition used
#SBATCH --chdir=/home/d669d153/work/phil.dicaeum/phylonet/nooutgroup	# Set working d$
#SBATCH --mem-per-cpu=5gb            # memory requested
#SBATCH --time=5000

module load java
java -jar /home/d669d153/work/PhyloNet_3.8.2.jar mpl.nooutgroup.1retic.nex

