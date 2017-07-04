import matplotlib.pyplot as plt
import subprocess
import sys
#print (sys.argv)

#gff_fh = open("GCF_000006945.1_ASM694v1_genomic.gff")
gff_fh = open(sys.argv[1])
gene_lengths = []

for line in gff_fh:
	if not line.startswith("#"):
		split_line = line.split()
		
		# separating genes from other stuff
		if split_line[2]== "gene":
			gene_start = int(split_line[3])
			gene_end = int(split_line[4])
			
			cur_gene_length = gene_end - gene_start
			gene_lengths.append(cur_gene_length)

#plotting length of genes
plt.hist(gene_lengths, bins=100)

filename = sys.argv[2]
plt.savefig(filename)

#Opening the pdf file on Acrobat Reader
subprocess.call(["AcroRd32",filename])
