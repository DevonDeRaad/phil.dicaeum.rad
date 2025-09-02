### This repository holds all of the details for the dadi modeling portion of the manuscript.

This is a general outline of the steps that I took:

- **step 1**: Build a custom script, (here it is the file: 'step1.prepare.snps.file.R'), that will take an input vcf and calculate the SNP count file that is needed for input to the Portik pipeline. For me, that resulted in the file 'dicaeum.snps.file.txt'.
          
- **step 2**: Run the script 'dadi-test-projections.py' (available here: https://github.com/dportik/dadi_pipeline/blob/master/Find-Best-Projections/dadi-test-projections.py) to identify the best combination of downsampling values to use for your dataset. For this dataset, the values that maximized the number of segregating sites was: (24, 52, 10).

- **step 3**: You now have the input data and know what values to use for down-projection, so you are ready to start running models. The original version of the script that is used to run 3-population models is called 'dadi_Run_3D_Set.py' (original version available here: https://github.com/dportik/dadi_pipeline/blob/master/Three_Population_Pipeline/dadi_Run_3D_Set.py). For this script to work, it needs to be modified according to the details of your project, and it needs to be located in the same directory as an unmodified version of the script 'Models_3D.py' (available here: https://github.com/dportik/dadi_pipeline/blob/master/Three_Population_Pipeline/Models_3D.py), which defines the models that you would like to run. In this same directory, you need to have an unmodified version of the script 'dadi_Run_Optimizations.py (available here: https://github.com/dportik/dadi_pipeline/blob/master/dadi_Run_Optimizations.py), which defines functions used internally to execute the model optimization routine defined by [Portik et al. 2017](https://onlinelibrary.wiley.com/doi/full/10.1111/mec.14266).

- ***note:*** Because these scripts are not multi-threaded, I set up a single script that contains the info for all models that I wanted to run, and then duplicated that script a bunch of times, named each one uniquely, and commented out all of the models except for one in each script. Finally, I ran each of these scripts individually on the UCLA cluster. This is a bit clunky, but it is the most effective way I've found to parallelize the pipeline. For this project, the full optimization protocol for some models took nearly 3 days to run, so by splitting up the 8 models into separate scripts, I was able to make the full run-time for optimizing all 8 models ~3 days, rather than ~2 weeks. For this project, the customized scripts I used are named:
   * run_refugia_adj_2.py
   * run_sim_split_no_mig.py
   * run_sim_split_refugia_sym_mig_adjacent.py
   * run_sim_split_sym_mig_adjacent.py
   * run_split_nomig.py
   * run_split_symmig_adjacent.py

Additionally, each of these python scripts executing a given model has a corresponding bash script used to execute it on the UCLA cluster with a 3-day wall clock so that the full optimization protocol can proceed to completion. These are named identically (e.g., 'run_split_nomig.py' was executed by submitting 'run_split_nomig.sh' as a job script).

- ***note 2:*** Because the splitting models imply that population 2 is geographically intermediate, but the admixed origin models imply that population 3 is the one derived from an admixed origin (see: https://github.com/dportik/dadi_pipeline/blob/master/Three_Population_Pipeline/Models_3D.pdf for details), I needed to set up a different input file where population 3 was the geographically intermediate population. I just manually did that (file named 'reordered.luz.zam.mind.dicaeum.snps.file.txt') and then pointed to that reordered input file in the python scripts where I ran the admixed origin models (I also changed the order of the downprojection values to match this updated order in these scripts):
    * run_admix_origin_no_mig.py
    * run_admix_origin_sym_mig_adj.py
          
- **step 4**: Once all of your models have finished the entire optimization protocol, you can see the output in the output files that end with the suffix 'optimized.txt' (e.g., 'pop1_pop2_pop3.split_nomig.optimized.txt' holds relevant output for the model 'split_nomig'). All eight of these output files generated here can be found in the folder 'output.files'.

- **step 5**: If you would like to generate a single summary table showing the details of all of your model optimization protocols, you can use the script 'Summarize_Outputs.py' (found here: https://github.com/dportik/dadi_pipeline/blob/master/Three_Population_Pipeline/Summarize_Outputs.py) to do so. 
          
- **step 6**: Visualize your best model using the python script 'Make_Plots.py' (available at: https://github.com/dportik/dadi_pipeline/blob/master/Plotting/Make_Plots.py). You will need to modify this script to include the details of your chosen model and the optimized parameter values you recovered. The unmodified script 'Plotting_Functions.py' (available at: https://github.com/dportik/dadi_pipeline/blob/master/Plotting/Plotting_Functions.py), which defines functions used internally in the plotting script, also needs to be present in the same directory where you execute 'Make_Plots.py' in order for it to work. The custom versions of the 'Make_Plots.py' scripts used here (which can be used to recreate the figures shown in the paper) are called:
    * XXX
    * 
          
- **step 7**: If you are interested in converting the estimated parameters for your best fit model into meaningful biological values,
          see this discussion: (https://github.com/dportik/dadi_pipeline/issues/5). Daniel Portik reccommends consulting the Dadi
          user group for more details. For this project I used the script 'scale.parameters.R' to perform conversions.
          
