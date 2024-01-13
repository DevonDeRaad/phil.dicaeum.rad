# Running SNAPP
* The input alignment for each replicate has the suffix '.nex' e.g., 'rep1.nex'.
* The input beauti file used to execute SNAPP for each replicate has the suffix '.xml' e.g., 'rep1.xml'.
* The output trees sampled from the posterior distribution for each replicate has the suffix '.trees' e.g., 'rep1.trees'.
* The output log file for each replicate used to assess convergence of the MCMC has the suffix '.log' e.g., 'rep1.log'.
* The concensus tree for each replicate has the suffix 'con.tree', e.g., 'rep1.con.tree'.
* All 20K post-burn-in trees are concatenated into a single file called 'all.reps.posterior.trees.gz'.
* The script used to execute all 5 SNAPP iterations on the KUHPCC is called 'snapp.array.sh'.
* A detailed vignette-style tutorial documenting the entire process can be viewed at: [https://devonderaad.github.io/phil.dicaeum.rad/snapp/run.snapp.html](https://devonderaad.github.io/phil.dicaeum.rad/run.snapp.html).
