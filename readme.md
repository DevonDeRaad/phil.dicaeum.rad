# The following repository holds all data and code for the manuscript:
Reconstructing the true evolutionary history of the Buzzing Flowerpecker (*Dicaeum hypoleucum*) despite extensive incomplete lineage sorting and ongoing gene flow.
- Lead author: Devon DeRaad (devonderaad@gmail.com)

### Data availability
* SNP datasets and sampling sheets can be found in the folder named [data](https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/data).
* fastq files containing all raw sequence data will be archived as a single BioProject via NCBI upon the acceptance of this manuscript.

### Lab protocols
* The detailed protocols used for DNA extraction and RADseq library prep can be found in the subdirectory called [lab.protocols](https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/lab.protocols).

### Sequence data to SNPs
* All code used to optimize the *de novo* assembly parameters during the [Stacks](https://catchenlab.life.illinois.edu/stacks/) RAD locus assembly, processing, and SNP calling pipeline can be found in the folder called [sequence.data.to.snps](https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/sequence.data.to.snps).
* A detailed walk-through with corresponding visualizations of the parameter optimization process can be found [here](https://devonderaad.github.io/phil.dicaeum.rad/sequence.data.to.snps/optimize.denovo.diacaeum.assembly.html).

### SNP filtering
* We used the R packages [vcfR](https://knausb.github.io/vcfR_documentation/) and [SNPfiltR](https://devonderaad.github.io/SNPfiltR/) to optimize and implement a series of SNP filtering thresholds. This entire protocol can be viewed at: [https://devonderaad.github.io/phil.dicaeum.rad/dicaeum.snp.filtering.html](https://devonderaad.github.io/phil.dicaeum.rad/dicaeum.snp.filtering.html).

### Sampling map
* Detailed code showing how I created the sampling map shown in the text can be viewed at: [https://devonderaad.github.io/phil.dicaeum.rad/make.sampling.map.html](https://devonderaad.github.io/phil.dicaeum.rad/make.sampling.map.html).

### Principal Components Analysis
* A vignette style tutorial detailing how I created the genomic PCA and calculated pairwise FST and fixed differences between clusters can be viewed at: [https://devonderaad.github.io/phil.dicaeum.rad/make.pca.html](https://devonderaad.github.io/phil.dicaeum.rad/make.pca.html).

### ADMIXTURE
* All input and output files associated with the ADMIXTURE runs presented in the text can be found in the folder named [admixture.mac](https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/admixture.mac). Additionally, a vignette style walk through of the process can be viewed [here](https://devonderaad.github.io/phil.dicaeum.rad/admixture.mac/run.admixture.html).

### mtDNA phylogenetics
* All input and output files associated mtDNA phylogenetic reconstructions can be found in the folder named [mtDNA.analyses]([https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/admixture.mac](https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/mtDNA.analyses).

### IQ-TREE 2 reconstruction
* The input and output files from the genomic phylogenetic reconstruction for all samples using IQ-TREE 2 can be found in the folder called [iqtree](https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/iqtree). A detailed walkthrough of the entire process is available [here](https://devonderaad.github.io/phil.dicaeum.rad/iqtree/run.iqtree.html).

### Unrooted phylogenetic network reconstruction
* A walkthrough of the process of creating the splitstree can be viewed at: [https://devonderaad.github.io/phil.dicaeum.rad/make.splitstree.html](https://devonderaad.github.io/phil.dicaeum.rad/make.splitstree.html).

### Species tree reconstruction from gene trees
* All input and output files associated with performing species tree reconstruction using [ASTRAL-III](https://github.com/smirarab/ASTRAL) can be found in the folder called [astral](https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/astral).
* A detailed walkthrough of the entire astral protocol can also be viewed [here](https://devonderaad.github.io/phil.dicaeum.rad/astral/run.astral.html).

### Species tree reconstruction from SNP data
* All input and output files associated with performing species tree reconstruction using [SNAPP](https://www.beast2.org/snapp/) can be found in the folder called [snapp](https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/snapp).
* A detailed walkthrough of the entire SNAPP protocol can also be viewed [here](https://devonderaad.github.io/phil.dicaeum.rad/snapp/run.snapp.html).

### ABBA/BABA tests using Dsuite
* All input and output files associated with running [Dsuite](https://github.com/millanek/Dsuite) can be found in the folder called [dsuite](https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/dsuite).
* A detailed walkthrough of how I ran Dsuite with detailed code can also be viewed [here](https://devonderaad.github.io/phil.dicaeum.rad/dsuite/run.dsuite.html).

### TreeMix analysis
* All input and output files associated with running [TreeMix](https://speciationgenomics.github.io/Treemix) can be found in the folder called [treemix](https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/treemix).
* A detailed walkthrough of the pipeline I used for running TreeMix, complete with visualizations of all output files, can be viewed [here](https://devonderaad.github.io/phil.dicaeum.rad/run.treemix.html).

### PhyloNet
* All input and output files for running [PhyloNet](https://phylogenomics.rice.edu/html/phylonet.html) can be found in the folder called [phylonet](https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/phylonet).
* A detailed walkthrough of the approach can be viewed [here](https://devonderaad.github.io/phil.dicaeum.rad/phylonet/runPhyloNet.html).

### Demographic modeling with PipeMaster
* A comprehensive explanation of our custom pipeline for performing demographic modeling using the program [PipeMaster](https://github.com/gehara/PipeMaster) is available in the subdirectory called [pipemaster](https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/pipemaster) which contains its own detailed 'readme' page.
