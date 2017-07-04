import pandas as pd

#reading the table
gene_data = pd.read_table("GCF_000006945.1_ASM694v1_genomic.gff", comment="#", names=["seq","source","feature","start","end","frame","strand","score","atributes"])
print(gene_data.columns)
print(gene_data.start) #gene_data["start"]

gene_data["gene_length"] = gene_data["end"] - gene_data["start"]

gene_data = gene_data[gene_data["feature"] == "gene"]

print(gene_data.head())