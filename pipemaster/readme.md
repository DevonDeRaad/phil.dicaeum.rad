This directory holds the information for running the program pipemaster to perform demographic modeling. For this manuscript, we designed a custom pipeline for creating the demographic models, tweaking/optimizing prior distributions for key parameters, and rigorously implementing the simulation and model selection approach. The details of each of these steps are outlined below:

## 1: Setting up demographic models
- The approach to setting up models in pipemaster can be challenging. Essentially the best approach is just to familiarize yourself with the overall structure of the model object, and manipulate it manually in R until you have the exact model and set of priors you want. Regularly using the PlotModel() function from the PipeMaster R package is key to making sure that you are actually setting up the model you're interested in correctly. For this dataset, example code outlining how I set up the four models I was interested in can be found at: XXX.
- 
