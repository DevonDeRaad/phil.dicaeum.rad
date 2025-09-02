
#read in vcf file
library(vcfR)
library(SNPfiltR)
v<-read.vcfR("~/Downloads/filtered.85.unlinked (2).vcf.gz")
#manually remove outgroup samples and remove invariant SNPs (should leave us with 2188 SNPs and 58 samples)
v<-v[,colnames(v@gt) != "D_nigrilore_KU28413" & colnames(v@gt) != "D_nigrilore_KU28414"]
v<-min_mac(v,min.mac = 1)
v

#extract genotype matrix
vmat<-extract.gt(v)
table(vmat, useNA = "always")
#convert '0/0' cells to 0
vmat[vmat == "0/0"]<-0
#convert 0/1 cells to 1
vmat[vmat == "0/1"]<-1
#convert 1/1 cells to 2
vmat[vmat == "1/1"]<-2
table(vmat, useNA = "always")
#convert matrix to numeric
vmat<-apply(vmat, 2, as.numeric)
table(vmat, useNA = "always")
#now have 'vmat' a numeric matrix showing the number of alt alleles sequenced for each sample at each snp (Genotype matrix)

#now identify which samples are part of each discrete population
#read in sample info:
samps<-read.csv("https://raw.githubusercontent.com/DevonDeRaad/phil.dicaeum.rad/refs/heads/main/data/dicaeum.retained.sampling.csv")
pop1.samps<-samps$ID[samps$Taxa == "Luzon"]
pop2.samps<-samps$ID[samps$Taxa == "Mindanao"]
pop3.samps<-samps$ID[samps$Taxa == "Zamboanga"]

#open up vector to hold each variable
Ingroup=c()
Outgroup=c()
Allele1=c()
pop1=c()
pop2=c()
pop3=c()
Allele2=c()
pop1alt=c()
pop2alt=c()
pop3alt=c()
Gene=c()
Position=c()

#for each SNP, get all this info:
for (i in 1:nrow(vmat)){
  Ingroup[i]<-paste0("-",v@fix[i,4],"-") #match portik formatting
  Outgroup[i]<-"---" #no info since SFS will be folded
  Allele1[i]<-v@fix[i,4] #record ref allele
  #record number of ref alleles. Equation is: (# hom. ref. genotypes*2 + # het. genotypes*1)
  pop1[i]<-sum(vmat[i,][colnames(vmat) %in% pop1.samps] == 0, na.rm = T)*2 + sum(vmat[i,][colnames(vmat) %in% pop1.samps] == 1, na.rm = T)
  pop2[i]<-sum(vmat[i,][colnames(vmat) %in% pop2.samps] == 0, na.rm = T)*2 + sum(vmat[i,][colnames(vmat) %in% pop2.samps] == 1, na.rm = T)
  pop3[i]<-sum(vmat[i,][colnames(vmat) %in% pop3.samps] == 0, na.rm = T)*2 + sum(vmat[i,][colnames(vmat) %in% pop3.samps] == 1, na.rm = T)
  Allele2[i]<-v@fix[i,5] #record alt allele
  pop1alt[i]<-sum(vmat[i,][colnames(vmat) %in% pop1.samps], na.rm = T) #count number of alt alleles in pop1
  pop2alt[i]<-sum(vmat[i,][colnames(vmat) %in% pop2.samps], na.rm = T) #count number of alt alleles in pop2
  pop3alt[i]<-sum(vmat[i,][colnames(vmat) %in% pop3.samps], na.rm = T) #count number of alt alleles in pop3
  Gene[i]<-v@fix[i,1] #record chrom
  Position[i]<-v@fix[i,2] #record position on chrom
}

#now combine the vectors into a single dataframe 
snps.file<-data.frame(Ingroup=Ingroup,
  Outgroup=Outgroup,
  Allele1=Allele1,
  pop1=pop1,
  pop2=pop2,
  pop3=pop3,
  Allele2=Allele2,
  pop1alt=pop1alt,
  pop2alt=pop2alt,
  pop3alt=pop3alt,
  Gene=Gene,
  Position=Position)

#check to make sure this looks right
head(snps.file)

#write to disk
write.table(snps.file,"~/Downloads/dicaeum.snps.file.txt",
            row.names = FALSE, quote = FALSE, sep = "\t")

#now you can just go manually remove the trailing 'alt' from the second set of population names
#(in the columns to the right of 'Allele2') and then you have an appropriately formatted SNPs
#input file for the portik Dadi pipeline.

