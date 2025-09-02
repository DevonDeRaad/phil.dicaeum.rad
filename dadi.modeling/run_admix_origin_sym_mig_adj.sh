#### submit_job.sh START ####
#!/bin/bash
#$ -cwd
#$ -o ./joblog.$JOB_ID.txt                   #set the job log output file
#$ -j y                                      #set error = Merged with joblog
#$ -l h_rt=72:00:00,h_data=10G,highp=TRUE      #specify requested resources (h_rt gives time request in 'hrs:mins:secs' format) (h_data specifies requested RAM per task) (highp=TRUE means run it on Aguillon Lab owned nodes)
#$ -pe shared 1                              #specify number of CPUs requested

#load necessary modules
. /u/local/Modules/default/init/modules.sh

#source python environment where all packages are installed:
module load python/3.6.8
source ~/.bashrc 

#run script
python3 run_admix_origin_sym_mig_adj.py
