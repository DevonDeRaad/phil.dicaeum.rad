#!/bin/sh
#
#SBATCH --job-name=optimize.M                           #Job Name
#SBATCH --nodes=1                                       #Request number of nodes
#SBATCH --cpus-per-task=25                              #CPU allocation per Task
#SBATCH --partition=bi                                  #Name of the Slurm partition used
#SBATCH --chdir=/home/d669d153/work/phil.dicaeum    	  #Set working directory
#SBATCH --mem-per-cpu=1gb                               #Memory requested
#SBATCH --time=5000                                    #Time requested

files="D_hypoleucum_18070
D_hypoleucum_18191
D_hypoleucum_14037
D_hypoleucum_14079
D_hypoleucum_14065
D_hypoleucum_14120
D_hypoleucum_17976
D_hypoleucum_18159
D_hypoleucum_14075
D_hypoleucum_20218
D_hypoleucum_19066
D_hypoleucum_19177
D_hypoleucum_19178
D_hypoleucum_14146
D_hypoleucum_20213
D_hypoleucum_FMNH454949
D_hypoleucum_25637
D_hypoleucum_1271
D_hypoleucum_1273
D_hypoleucum_1275
D_hypoleucum_25921
D_hypoleucum_3274
D_hypoleucum_26984
D_hypoleucum_3208
D_hypoleucum_3158
D_hypoleucum_2253
D_hypoleucum_3095
D_hypoleucum_462070
D_hypoleucum_25675
D_hypoleucum_454950
D_hypoleucum_25880
D_hypoleucum_3314
D_hypoleucum_357608
D_hypoleucum_357615
D_hypoleucum_357612
D_hypoleucum_19638
D_hypoleucum_25868
D_hypoleucum_17969
D_hypoleucum_25672
D_hypoleucum_26975
D_hypoleucum_2229
D_hypoleucum_2067
D_hypoleucum_28329
D_hypoleucum_28361
D_hypoleucum_28376
D_hypoleucum_2208
D_hypoleucum_28294
D_hypoleucum_1956
D_hypoleucum_25670
D_hypoleucum_20921
D_hypoleucum_20193
D_hypoleucum_28416
D_hypoleucum_18193
D_hypoleucum_27450
D_hypoleucum_19046
D_hypoleucum_19136
D_hypoleucum_28663
D_hypoleucum_28676
D_nigrilore_KU28413
D_nigrilore_KU28414
D_hypoleucum_29945
D_hypoleucum_31636
D_hypoleucum_29951
D_hypoleucum_31644"

# Build loci de novo in each sample for the single-end reads only.
# -M — Maximum distance (in nucleotides) allowed between stacks (default 2).
# -m — Minimum depth of coverage required to create a stack (default 3).
#here, we will vary m from 3-7, and leave all other paramaters default

for i in {1..8}
do
#create a directory to hold this unique iteration:
mkdir stacks_bigM$i
#run ustacks with m equal to the optimized value, and 
id=1
for sample in $files
do
    /home/d669d153/work/stacks-2.41/ustacks -f fastq/${sample}.fq.gz -o stacks_bigM$i -i $id -m 5 -M $i -p 25
    let "id+=1"
done
## Run cstacks to compile stacks between samples. Popmap is a file in working directory called 'pipeline_popmap.txt'
/home/d669d153/work/stacks-2.41/cstacks -P stacks_bigM$i -M pipeline_popmap.txt -p 25
## Run sstacks. Match all samples supplied in the population map against the catalog.
/home/d669d153/work/stacks-2.41/sstacks -P stacks_bigM$i -M pipeline_popmap.txt -p 25
## Run tsv2bam to transpose the data so it is stored by locus, instead of by sample.
/home/d669d153/work/stacks-2.41/tsv2bam -P stacks_bigM$i -M pipeline_popmap.txt -t 25
## Run gstacks: build a paired-end contig from the metapopulation data (if paired-reads provided),
## align reads per sample, call variant sites in the population, genotypes in each individual.
/home/d669d153/work/stacks-2.41/gstacks -P stacks_bigM$i -M pipeline_popmap.txt -t 25
## Run populations completely unfiltered and output unfiltered vcf, for input to the RADstackshelpR package
/home/d669d153/work/stacks-2.41/populations -P stacks_bigM$i -M pipeline_popmap.txt --vcf -t 25
done

