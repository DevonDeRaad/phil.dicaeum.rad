# Data and code for the manuscript:
Reconstructing the true evolutionary history of the Buzzing Flowerpecker (*Dicaeum hypoleucum*) despite extensive incomplete lineage sorting and ongoing gene flow

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

