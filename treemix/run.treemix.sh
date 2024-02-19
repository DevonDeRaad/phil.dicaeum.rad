#!/bin/sh
#
#SBATCH --job-name=treemix              # Job Name
#SBATCH --nodes=1             # 40 nodes
#SBATCH --ntasks-per-node=1               # 40 CPU allocation per Task
#SBATCH --partition=sixhour            # Name of the Slurm partition used
#SBATCH --chdir=/home/d669d153/work/phil.dicaeum/treemix     # Set working d$
#SBATCH --mem-per-cpu=5gb           # memory requested
#SBATCH --time=100

#convert vcf into treemix file
#/home/d669d153/work/stacks-2.41/populations --in_vcf filtered.85.unlinked.vcf -O . --treemix -M treemix.popmap.txt
#remove stacks header
#echo "$(tail -n +2 filtered.85.unlinked.p.treemix)" > filtered.85.unlinked.p.treemix
#gzip file for input to treemix
#gzip filtered.85.unlinked.p.treemix

#run treemix with m0
/panfs/pfs.local/work/bi/bin/treemix-1.13/src/treemix -i filtered.85.unlinked.p.treemix.gz -root nigrilore -o treem0

#add 1 migration edge
/panfs/pfs.local/work/bi/bin/treemix-1.13/src/treemix -i filtered.85.unlinked.p.treemix.gz -m 1 -g treem0.vertices.gz treem0.edges.gz -o treem1

#add 2 migration edges
/panfs/pfs.local/work/bi/bin/treemix-1.13/src/treemix -i filtered.85.unlinked.p.treemix.gz -m 1 -g treem1.vertices.gz treem1.edges.gz -o treem2

#add 3 migration edges
/panfs/pfs.local/work/bi/bin/treemix-1.13/src/treemix -i filtered.85.unlinked.p.treemix.gz -m 1 -g treem2.vertices.gz treem2.edges.gz -o treem3

