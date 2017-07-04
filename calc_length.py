import matplotlib.pyplot as plt

gff_fh = open("GCF_000006945.1_ASM694v1_genomic.gff")
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

#print(gene_lengths)
#plotting length of genes
plt.hist(gene_lengths)
plt.savefig("gene_length_hist.pdf")