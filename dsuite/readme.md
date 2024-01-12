# Running Dsuite
### Input files
* I used our [filtered SNP dataset](https://github.com/DevonDeRaad/phil.dicaeum.rad/blob/main/data/filtered.85.vcf.gz) as input for Dsuite.
* The guide tree I specified is found in the file 'nwk.tre'.
* The sample assignments are found in the file 'pops.txt'
### Output files
* The file 'pops_with.mtbusa_tree.txt' contains the output D statistic and corresponding p-value for the ABBA/BABA test performed in accordance with the pre-specified tree (i.e., the one used in the manuscript).
### Removing Mt. Busa
* All critical input and output files from the subsequent run after removing the five samples from Mt. Busa can be found in the folder called 'nomtbusa'.
### Full walkthrough
* A detailed walkthrough of the entire process of running Dsuite is available at: [https://devonderaad.github.io/phil.dicaeum.rad/dsuite/run.dsuite.html](https://devonderaad.github.io/phil.dicaeum.rad/dsuite/run.dsuite.html).
