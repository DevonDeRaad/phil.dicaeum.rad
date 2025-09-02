'''
Usage: python Make_Plots.py

This is meant to be a general use script to fit a demographic model and create
plots of the data and model sfs. The user will have to edit information about
their allele frequency spectrum and provide a custom model. The instructions
are annotated below, with a #************** marking sections that will have to
be edited.

This script must be in the same working directory as Plotting_Functions.py, which
contains all the functions necessary for generating simulations and optimizing the model.

General workflow:
 The user provides a model and the previously optimized parameters for their empirical 
 data. The model is fit using these parameters, and the resulting model SFS is used to
 create the plot comparing the data to the model. 
 
Outputs:
 A summary file of the model fit will be created, along with a pdf of the plot.
 
Notes/Caveats:
 Sometimes you may see the following error when plotting 2D or 3D:
 
 "ValueError: Data has no positive values, and therefore can not be log-scaled."
 
 To deal with this, you can change the optional argument vmin_val to a value
 between 0 and 0.05 (0.05 is the default). I have used values from 0.005-0.01
 with good visual results.

Citations:
 If you use these scripts for your work, please cite the following publications.
 
'''
import os
import numpy
import dadi
import Plotting_Functions
from dadi import Numerics, PhiManip, Integration, Misc
from dadi.Spectrum_mod import Spectrum

#===========================================================================
# Import data to create joint-site frequency spectrum
#===========================================================================

#**************
#path to your input file
snps = "/Users/devonderaad/Downloads/dicaeum_test/dicaeum.snps.file.txt"

#Create python dictionary from snps file
dd = Misc.make_data_dict(snps)

#**************
#pop_ids is a list which should match the populations headers of your SNPs file columns
pop_ids=['pop1','pop2','pop3']

#**************
#projection sizes, in ALLELES not individuals
proj = [24,52,10]

#Convert this dictionary into folded AFS object
#[polarized = False] creates folded spectrum object
fs = Spectrum.from_data_dict(dd, pop_ids=pop_ids, projections = proj, polarized = False)

#print some useful information about the afs or jsfs
print("\n\n============================================================================")
print("\nData for site frequency spectrum:\n")
print("Projection: {}".format(proj))
print("Sample sizes: {}".format(fs.sample_sizes))
print("Sum of SFS: {}".format(numpy.around(fs.S(), 2)))
print("\n============================================================================\n")


#================================================================================
# Fit the empirical data based on prior optimization results, obtain model SFS
#================================================================================
''' 
 We will use a function from the Plotting_Functions.py script:
 	Fit_Empirical(fs, pts, outfile, model_name, func, in_params, fs_folded)

Mandatory Arguments =
 	fs:  spectrum object name
 	pts: grid size for extrapolation, list of three values
 	outfile: prefix for output naming
 	model_name: a label to help name the output files; ex. "sym_mig"
 	func: access the model function from within script
 	in_params: the previously optimized parameters to use
    fs_folded: A Boolean value indicating whether the empirical fs is folded (True) or not (False).
'''

#**************
#COPY AND PASTE YOUR MODEL HERE, do not use this one!
#you can copy/paste directly from the Models_2D.py or Models_3D.py scripts

def split_symmig_adjacent(params, ns, pts):
    """
    Model with split between pop 1 and (2,3), then split between 2 and 3. Assume 2 occurs
    in between populations 1 and 3, which do not come in to contact with one another.
    Migration is symmetrical between 'adjacent' population pairs (ie 1<->2, 2<->3, but not 1<->3).
    nu1: Size of population 1 after split.
    nuA: Size of population (2,3) after split from 1.
    nu2: Size of population 2 after split.
    nu3: Size of population 3 after split.
    mA: Migration rate between population 1 and population (2,3)
    m1: Migration rate between populations 1 and 2 (2*Na*m) 
	m2: Migration rate between populations 2 and 3 
    m3: Migration rate between populations 1 and 3
    T1: The scaled time between the split of pops 1 vs 2 and 3 (in units of 2*Na generations).
    T2: The scaled time between the split of pops 2 and 3 (in units of 2*Na generations).
   """
    #9 parameters
    nu1, nuA, nu2, nu3, mA, m1, m2, T1, T2 = params

    xx = Numerics.default_grid(pts)
    phi = PhiManip.phi_1D(xx)
    phi = PhiManip.phi_1D_to_2D(xx, phi)

    phi = Integration.two_pops(phi, xx, T1, nu1=nu1, nu2=nuA, m12=mA, m21=mA)

    phi = PhiManip.phi_2D_to_3D_split_2(xx, phi)
    
    phi = Integration.three_pops(phi, xx, T2, nu1=nu1, nu2=nu2, nu3=nu3, m12=m1, m21=m1, m23=m2, m32=m2, m13=0, m31=0)

    fs = Spectrum.from_phi(phi, ns, (xx,xx,xx))
    return fs

#create a prefix based on the population names to label the output files
#ex. Pop1_Pop2
#DO NOT EDIT THIS
prefix = "_".join(pop_ids)

#**************
#Make sure to define your extrapolation grid size.
pts = [50,60,70]

#**************
#Provide best optimized parameter set for empirical data.
#These will come from previous analyses you have already completed.
emp_params = [7.8038, 0.4988, 11.8617, 1.3706, 0.5652, 0.2392, 0.0962, 0.1419, 1.454]

#**************
#Fit the model using these parameters and return the model SFS.
#Here, you will want to change the "sym_mig" and sym_mig arguments to match your model, but
#everything else can stay as it is. See above for argument explanations.
model_fit = Plotting_Functions.Fit_Empirical(fs, pts, prefix, "split_symmig_adjacent", split_symmig_adjacent, emp_params, fs_folded=True)


#================================================================================
# Plotting a 3D spectrum
#================================================================================

#Although we've used the script to plot a 2D jsfs, it can also be used to create
#plots a 3D spectrum in much the same way.

'''
For a 3D jsfs:
 We will use a function from the Plotting_Functions.py script to plot:
 	Plot_3D(fs, model_fit, outfile, model_name, vmin_val=None)

 Mandatory Arguments =
	fs:  spectrum object name
    model_fit:  the model spectrum object name
 	outfile: prefix for output naming
 	model_name: a label to help name the output files; ex. "sym_mig"

 Optional Arguments =
     vmin_val: Minimum values plotted for sfs, default is 0.05 and to fix the common error this should
               be changed to something between 0 and 0.05.
'''

#Example 3D plot call (will not work with the example 2D sfs!):
#**************
#Unhash the command below to run the 3D plot, make sure to change
#the 'prefix' and 'something' args to fit your dataset 

Plotting_Functions.Plot_3D(fs, model_fit, prefix, "no_mig", 0.05)

