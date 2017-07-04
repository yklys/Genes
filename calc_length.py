gff_fh = open("GCF_000006945.1_ASM694v1_genomic.gff")
gene_lengths = []

for line in gff_fh:
	if not line.startswith("#"):
		split_line = line.split()
		
		if split_line[2]== "gene":
			gene_start = int(split_line[3])
			gene_end = int(split_line[4])
			cur_gene_length = gene_end - gene_start

			#print("Gene start:",gene_start,"Gene end:",gene_end,"\nGene size: ",cur_gene_length)
			gene_lengths.append(cur_gene_length)

print(gene_lengths)