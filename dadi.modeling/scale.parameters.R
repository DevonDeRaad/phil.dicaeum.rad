#scale parameter estimates to interpretable values:

#For the model 'split_symmig_adjacent'
#calc 'nref'
#theta=4*nref*u*l
theta<-58.05 #taken from the output file
u<-4.6e-09 #taken from Smeds et al. 2016
l<-2188*100 #number of RAD loci * length
nref<-theta/(4*u*l)
nref #print nref

#9 parameters
#nu1, nuA, nu2, nu3, mA, m1, m2, T1, T2 = params
#vals:7.8038,0.4988,11.8617,1.3706,0.5652,0.2392,0.0962,0.1419,1.454
#nu1
7.8038*nref
#nuA
0.4988*nref
#nu2
11.8617*nref
#nu3
1.3706*nref
#mA rate = Ma/(2*Nref) 
0.5652/(2*nref)
#m1
0.2392/(2*nref)
#m2
0.0962/(2*nref)
#T1
0.1419*2*nref
#T2
1.454*2*nref


#For the model 'sim_split_refugia_sym_mig_adjacent'
#calc 'nref'
#theta=4*nref*u*l
theta<-96.92 #taken from the output file
u<-4.6e-09 #taken from Smeds et al. 2016
l<-2188*100 #number of RAD loci * length
nref<-theta/(4*u*l)
nref #print nref

#7 parameters
#nu1, nu2, nu3, m1, m2, T1, T2 = params
#vals: 4.6484, 8.9103, 0.7089, 0.5831, 0.4616, 0.6037, 0.0928

#nu1
4.6484*nref
#nu2
8.9103*nref
#nu3
0.7089*nref
#m1
0.5831/(2*nref)
#m2
0.4616/(2*nref)
#T1
0.6037*2*nref
#T2
0.0928*2*nref



