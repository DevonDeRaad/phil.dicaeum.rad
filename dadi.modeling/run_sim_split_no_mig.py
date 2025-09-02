'''
Devon DeRaad
22 August 2025

This is my custom version of the script 'dadi_Run_3D_Set.py' (original version at:
https://github.com/dportik/dadi_pipeline/blob/master/Three_Population_Pipeline/dadi_Run_3D_Set.py).

The actual models are stored in the script 'Models_3D.py' (original version can be downloaded from:
https://github.com/dportik/dadi_pipeline/blob/master/Three_Population_Pipeline/Models_3D.py)
which must be stored in the same working directory as this script, in order to run properly.
The script 'Models_3D.py' never needs to be modified in any way, simply remove the code at the
end of *this script* (the one you're currently in) to avoid running running any models
that you aren't interested in.

The current script must also be located in the same working directory as the script 'Optimize_Functions.py'
(download here: https://github.com/dportik/dadi_pipeline/blob/master/Optimize_Functions.py), which
will be used to import many of the specific functions used below.

General workflow:
 The optimization routine runs a user-defined number of rounds, each with a user-defined
 or predefined number of replicates. The starting parameters are initially random, but after
 each round is complete the parameters of the best scoring replicate from that round are
 used to generate perturbed starting parameters for the replicates of the subsequent round.
 
 Each round should continuously converge on smaller AIC scores. The lowest overall AIC score
 recovered for a given model can be considered the 'best fit' for that model. The best fit
 for each model can then be compared to determine which demographic model best explains the data.
'''

#each of these lines is the equivalent of running 'library()' in R and loading a given package
import sys
import os
import numpy
import dadi
from datetime import datetime
#the following are not libraries or packages, but scripts. Therefore, these lines won't work unless there is a script in your working directory named:
#'Optimize_Functions.py' (this can be downloaded here: https://github.com/dportik/dadi_pipeline/blob/master/Optimize_Functions.py)
import Optimize_Functions
#This import requires the script 'Models_3D.py' to be in your working directory. This script should be modified to only include models you want to test
#(download here: https://github.com/dportik/dadi_pipeline/blob/master/Three_Population_Pipeline/Models_3D.py)
import Models_3D

#===========================================================================
# Import data to create joint-site frequency spectrum
#===========================================================================

#specify path to input SNP file
snps = "/u/project/aguillon/dderaad/phil.dicaeum.dadi/dicaeum.snps.file.txt"

#Create python dictionary from snps file
dd = dadi.Misc.make_data_dict(snps)

#Specify the two populations in your SNPs file
#pop_ids is a list which should match the populations headers of your SNPs file columns
#the order specified here determines the ID of each population in the models, i.e.,
#the order should match assignment into pop1, pop2, and pop3 in the models,
#see (https://github.com/dportik/dadi_pipeline/blob/master/Three_Population_Pipeline/Models_3D.pdf)
#for exact details on which population does what in each model, for instance:
#tree structure is always (pop1,(pop2,pop3)) in each bifurcating model.
#here, I'm specifying pop1 (Luzon) as first branching:
pop_ids=['pop1','pop2','pop3']

#Specify the projection sizes you've chosen based on:
#(https://github.com/dportik/dadi_pipeline/tree/master/Find-Best-Projections)
#projection sizes, specified in ALLELES, not individuals
# *** order must match the order that the pops were specified in 'pop_ids' ***
proj = [24,52,10]

#Convert this dictionary into folded AFS object
#[polarized = False] creates folded spectrum object
fs = dadi.Spectrum.from_data_dict(dd, pop_ids=pop_ids, projections = proj, polarized = False)

#print some useful information about the afs or jsfs
print("\n\n============================================================================")
print("\nData for site frequency spectrum:\n")
print("Projection: {}".format(proj))
print("Sample sizes: {}".format(fs.sample_sizes))
print("Sum of SFS: {}".format(numpy.around(fs.S(), 2)))
print("\n============================================================================\n")

#===========================================================================
# Set up optimization parameters
#===========================================================================
'''
 We will use a function from the Optimize_Functions.py script for our optimization routines:
 
 Optimize_Routine(fs, pts, outfile, model_name, func, rounds, param_number, fs_folded=True, 
                      reps=None, maxiters=None, folds=None, in_params=None, 
                      in_upper=None, in_lower=None, param_labels=None, optimizer="log_fmin")
 
   Mandatory Arguments =
    fs:  spectrum object name
    pts: grid size for extrapolation, list of three values
    outfile:  prefix for output naming
    model_name: a label to help label the output files; ex. "no_mig"
    func: access the model function from within 'moments_Run_Optimizations.py' or from a separate python model script, 
          ex. after importing Models_3D, calling Models_3D.split_nomig
    rounds: number of optimization rounds to perform
    param_number: number of parameters in the model selected (can count in params line for the model)
    fs_folded: A Boolean value (True or False) indicating whether the empirical fs is folded (True) or not (False).

   Optional Arguments =
     reps: a list of integers controlling the number of replicates in each of the optimization rounds
     maxiters: a list of integers controlling the maxiter argument in each of the optimization rounds
     folds: a list of integers controlling the fold argument when perturbing input parameter values
     in_params: a list of parameter values 
     in_upper: a list of upper bound values
     in_lower: a list of lower bound values
     param_labels: list of labels for parameters that will be written to the output file to keep track of their order
     optimizer: a string, to select the optimizer. Choices include: "log" (BFGS method), "log_lbfgsb" (L-BFGS-B method), 
                "log_fmin" (Nelder-Mead method), and "log_powell" (Powell's method).

'''

#create a prefix based on the population names to label the output files
#ex. Pop1_Pop2_Pop3
prefix = "_".join(pop_ids)

#**************
#make sure to define your extrapolation grid size (based on your projections)
#(Default values are 50,60,70)
pts = [50,60,70]

#**************
#Set the number of rounds here
#(Default = 4)
rounds = 4

#define the lists for optional arguments
#you can change these to alter the settings of the optimization routine
reps = [10,20,30,40]
maxiters = [3,5,10,15]
folds = [3,2,2,1]

#**************
#Indicate whether your frequency spectrum object is folded (True) or unfolded (False)
fs_folded = True


#================================================================================
# Calling external 3D models from the script 'Models_3D.py'
#================================================================================


# Split into three populations, no migration.
#Optimize_Functions.Optimize_Routine(fs, pts, prefix, "split_nomig", Models_3D.split_nomig, rounds, 6, fs_folded=fs_folded,
#                                        reps=reps, maxiters=maxiters, folds=folds, param_labels = "nu1, nuA, nu2, nu3, T1, T2")

# Split into three populations, symmetric migration between 'adjacent' populations (1<->2, 2<->3, but not 1<->3).
#Optimize_Functions.Optimize_Routine(fs, pts, prefix, "split_symmig_adjacent", Models_3D.split_symmig_adjacent, rounds, 9, fs_folded=fs_folded,
#                                        reps=reps, maxiters=maxiters, folds=folds, param_labels = "nu1, nuA, nu2, nu3, mA, m1, m2, T1, T2")
                                        
# Adjacent Secondary contact, shorter isolation - Split between pop 1 and (2,3), gene flow does not occur. Split between pop 2 and 3 occurs with gene flow. After appearance of 2 and 3, gene flow also occurs between 1 and 2.
#Optimize_Functions.Optimize_Routine(fs, pts, prefix, "refugia_adj_2", Models_3D.refugia_adj_2, rounds, 8, fs_folded=fs_folded,
#                                        reps=reps, maxiters=maxiters, folds=folds, param_labels = "nu1, nuA, nu2, nu3, m1, m2, T1, T2")

# Simultaneous split into three populations, no migration.
Optimize_Functions.Optimize_Routine(fs, pts, prefix, "sim_split_no_mig", Models_3D.sim_split_no_mig, rounds, 4, fs_folded=fs_folded,
                                        reps=reps, maxiters=maxiters, folds=folds, param_labels = "nu1, nu2, nu3, T1")

# Simultaneous split into three populations, symmetric migration between 'adjacent' populations (1<->2, 2<->3, but not 1<->3).
#Optimize_Functions.Optimize_Routine(fs, pts, prefix, "sim_split_sym_mig_adjacent", Models_3D.sim_split_sym_mig_adjacent, rounds, 6, fs_folded=fs_folded,
#                                        reps=reps, maxiters=maxiters, folds=folds, param_labels = "nu1, nu2, nu3, m1, m2, T1")

# Simultaneous split into three populations, secondary contact between 'adjacent' populations (1<->2, 2<->3, but not 1<->3).
#Optimize_Functions.Optimize_Routine(fs, pts, prefix, "sim_split_refugia_sym_mig_adjacent", Models_3D.sim_split_refugia_sym_mig_adjacent, rounds, 7, fs_folded=fs_folded,
#                                        reps=reps, maxiters=maxiters, folds=folds, param_labels = "nu1, nu2, nu3, m1, m2, T1, T2")

### Hybrid origin models ###

#these need to be run in a separate script, because the population order needs to be different
#for these models, the hybrid pop is pop3, and I have it set up above where the geographically intermediate pop is pop2

#up = [20, 20, 20, 10, 10, 0.999]
#ps = [1, 1, 1, 1, 1, 0.5]
#Optimize_Functions.Optimize_Routine(fs, pts, prefix, "admix_origin_no_mig", Models_3D.admix_origin_no_mig, rounds, 6, fs_folded=fs_folded,
#                                        reps=reps, maxiters=maxiters, folds=folds, param_labels = "nu1, nu2, nu3, T1, T2, f", in_upper=up, in_params=ps)

#up = [20, 20, 20, 20, 20, 10, 10, 0.999]
#ps = [1, 1, 1, 1, 1, 1, 1, 0.5]
#Optimize_Functions.Optimize_Routine(fs, pts, prefix, "admix_origin_sym_mig_adj", Models_3D.admix_origin_sym_mig_adj, rounds, 8, fs_folded=fs_folded,
#                                        reps=reps, maxiters=maxiters, folds=folds, param_labels = "nu1, nu2, nu3, m1, m3, T1, T2, f", in_upper=up, in_params=ps)

