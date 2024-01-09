# Data

This repository contains the data necessary to recreate the analyses performed in this manuscript.

### Raw SNP data
* Raw, unfiltered SNP data generated using the optimal set of parameters for *de novo* RAD locus assembly is contained in the file 'n8.vcf.gz'. The dataset contains 250,231 SNPs found on 47,564 loci, shared across 64 samples, with 58% overall missing data.

### Filtered SNP data
* Filtered SNP data is found in the file named 'filtered.85.vcf.gz'. This file contains 18,499 SNPs found on 2,590 loci, shared by 60 samples used in dowsntream analyses, with 10.85% overall missing data.

### Filtered, unlinked SNP data
* Filtered SNP data is found in the file named 'filtered.85.unlinked.vcf.gz'. This file contains 2,590 SNPs shared by 60 samples used in dowsntream analyses, with 11.18% overall missing data. These SNPs are putatively unlinked, as it has been filtered to retain only a single SNP per *de novo* assembled locus.

### All sample info
* Details on all 82 sequenced samples for this project can be found in the file named 'phil.dicaeum.82samps.csv'. This includes information on whether the sample made it through filtering, or details on why it was subsequently dropped from the dataset.

### Final filtered sample info
* Details (inlcuding exact lat/longs used for mapping) on the 60 samples used in downstream analyses can be found in the file called 'dicaeum.retained.sampling.csv'.
