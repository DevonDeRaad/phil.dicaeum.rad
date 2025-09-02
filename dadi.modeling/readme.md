### This repository holds all of the details for the dadi modeling portion of the manuscript.

This is a general outline of the steps that I took:

- step 1: Build a custom script, (here it is the file: 'step1.prepare.snps.file.R'), that will take an input vcf and calculate the SNP count file
          that is needed for input to the Portik pipeline. For me, that resulted in the file 'dicaeum.snps.file.txt'.
          
- step 2: Run the script 'dadi-test-projections.py'
          (available here: https://github.com/dportik/dadi_pipeline/blob/master/Find-Best-Projections/dadi-test-projections.py)
          to identify the best combination of downsampling values to use for your dataset. For this dataset, the values that
          maximized the number of segregating sites was: (24, 52, 10).

- step 3: You now have the input data and know what values to use for down-projection, so you are ready to start running models.
          You should set up a single script that contains the info for each model you want to run.
          Then, I just duplicated that script a bunch of times, named each one uniquely, and comment out all of the models except
          for the one you want to run. Because the program is not multi-threaded, making these duplicate scripts and then running all of them at
          the same time is the most effective way to run the pipeline in parallel. For this project, these files are:
            -XXXX
            -XXXX
            -XXXX
          
- step 4: Once all of your models have finished the entire optimization protocol, you can use the script 'Summarize_Outputs.py'
          (found here: https://github.com/dportik/dadi_pipeline/blob/master/Three_Population_Pipeline/Summarize_Outputs.py)
          To summarize all of your results.
          
- step 5: Visualize your best model using the python script 'Make_Plots.py' (available at: 
          https://github.com/dportik/dadi_pipeline/blob/master/Plotting/Make_Plots.py). 
          
- step 6: If you are interested in converting the estimated parameters for your best fit model into meaningful biological values,
          see this discussion: (https://github.com/dportik/dadi_pipeline/issues/5). Daniel Portik reccommends consulting the Dadi
          user group for more details. For this project I used the script 'scale.parameters.R' to perform conversions.
          
