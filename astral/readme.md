# ASTRAL-III species tree reconstruction
* The input file used to generate individual fasta and nexus alignments to create gene trees is called 'pops.phy.gz'.
* This alignmment can be cut up into separate locus alignments using the info found in the file 'populations.all.partitions.phylip'.
* The resulting species tree with posterior probabilities is found in the file 'species_pp.tree'.
* The same tree made after contracting low (< 10) BS support branches in input gene trees is called 'species_pp_BS10.tree'.
* The quartet frequencies for this tree are found in the file 'freq.quad.txt'.
* The results of the polytomy test (ASTRAL-III flag 't -10') can be found in the file 'astral.polytomy.tre'.

### Removing Mt. Busa samples
* The species tree after running the same analysis with the 5 samples from Mt. Busa removed is called 'no.mtbusa.astral.tree'.
* The quartet frequencies after the Mt. Busa samples are removed can be found in the file called 'no.mtbusa.freqQuad.txt'.
* The results of the polytomy test (ASTRAL-III flag 't -10') can be found in the file 'no.mtbusa.polytomy.tre'.

### Full walkthrough
* A complete vignette style walkthrough of this entire process can be viewed at [https://devonderaad.github.io/phil.dicaeum.rad/astral/run.astral.html](https://devonderaad.github.io/phil.dicaeum.rad/astral/run.astral.html).
