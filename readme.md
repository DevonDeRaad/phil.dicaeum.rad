# Data and code for the manuscript:
Reconstructing the true evolutionary history of the Buzzing Flowerpecker (*Dicaeum hypoleucum*) despite extensive incomplete lineage sorting and ongoing gene flow

### Data availability
* SNP datasets and sampling sheets can be found in the folder named [data](https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/data).
* fastq files containing all raw sequence data will be archived as a single BioProject via NCBI upon the acceptance of this manuscript.

### Sequence data to SNPs
* All code used to optimize the *de novo* assembly parameters during the [Stacks](https://catchenlab.life.illinois.edu/stacks/) RAD locus assembly, processing, and SNP calling pipeline can be found in the folder called [sequence.data.to.snps](https://github.com/DevonDeRaad/phil.dicaeum.rad/tree/main/sequence.data.to.snps).
* A detailed walk-through with corresponding visualizations of the parameter optimization process can be found [here](https://devonderaad.github.io/phil.dicaeum.rad/sequence.data.to.snps/optimize.denovo.diacaeum.assembly.html).

### SNP filtering
* We used the R packages [vcfR](https://knausb.github.io/vcfR_documentation/) and [SNPfiltR](https://devonderaad.github.io/SNPfiltR/) to optimize and implement a series of SNP filtering thresholds. This entire protocol can be viewed at: [https://devonderaad.github.io/phil.dicaeum.rad/dicaeum.snp.filtering.html](https://devonderaad.github.io/phil.dicaeum.rad/dicaeum.snp.filtering.html).
