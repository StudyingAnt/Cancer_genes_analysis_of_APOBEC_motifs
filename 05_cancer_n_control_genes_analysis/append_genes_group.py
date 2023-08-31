import pandas as pd
from pathlib import Path, PurePath

import re

input_dir = "/mnt/c/Users/CEEL-PC-005/Desktop/Joon/projects/cancer_evolution_robustness_evolvability_files/CDUR_cancer_vs_control/in"
output_dir = "/mnt/c/Users/CEEL-PC-005/Desktop/Joon/projects/cancer_evolution_robustness_evolvability_files/CDUR_cancer_vs_control/out"

gencode_cdur_file = PurePath(input_dir, "CDUR_cleaned_gencode_pc_transcript_refseq.tsv")
cancer_no_mutation_file = PurePath(input_dir, "ncbi_human_clean_no_mutation_2_protein_coding_no_LOC_no_MT.tsv")
cancer_census_file = PurePath(input_dir, "cancer_gene_census_ovarian.csv")

gencode_cdur = pd.read_csv(gencode_cdur_file, sep="\t")
cancer_no_mutation = pd.read_csv(cancer_no_mutation_file, sep="\t")
cancer_census = pd.read_csv(cancer_census_file)

gencode_lst = [item[:len(item)-4] for item in gencode_cdur["Protein"].to_list()]
cancer_census_lst = cancer_census["Gene Symbol"].to_list()
cancer_no_mut_list = cancer_no_mutation["symbol"].to_list()

index_lst = [key for key, val in enumerate(gencode_lst) if val in set(cancer_no_mut_list)]
val_lst = [val for key, val in enumerate(gencode_lst) if val in set(cancer_no_mut_list)]

print(val_lst)

index_lst2 = [key for key, val in enumerate(gencode_lst) if val in set(cancer_census_lst)]
val_lst2 = [val for key, val in enumerate(gencode_lst) if val in set(cancer_census_lst)]

gene_class = []
for i in range(len(gencode_cdur["Protein"].to_list())):
    if i in index_lst:
        gene_class.append("control")
    elif i in index_lst2:
        gene_class.append("cancer")
    else:
        gene_class.append("regular")

gencode_cdur["gene_class"] = gene_class

output_file = PurePath(input_dir, "CDUR_cleaned_gencode_pc_transcript_refseq_gene_class_ovarian.tsv")
#gencode_cdur.to_csv(output_file, index=False, sep="\t")

val_lst3 = [val for key, val in enumerate(cancer_no_mut_list) if val not in set(val_lst)]
#print(val_lst3)


output_file = PurePath(input_dir, "CDUR_cleaned_gencode_pc_transcript_refseq_cancer_no_mut.tsv")
output_file2 = PurePath(input_dir, "CDUR_cleaned_gencode_pc_transcript_refseq_cancer_census.tsv")
#gencode_cdur.iloc[index_lst].to_csv(output_file, index=False, sep="\t")
#gencode_cdur.iloc[index_lst2].to_csv(output_file2, index=False, sep="\t")


#print(gencode_cdur["Protein"].to_list())
#print([item[:len(item)-4  ] for item in gencode_cdur["Protein"].to_list()])
#print(cancer_no_mutation)