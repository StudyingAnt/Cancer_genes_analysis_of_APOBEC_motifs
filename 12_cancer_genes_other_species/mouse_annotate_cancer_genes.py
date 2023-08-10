import pandas as pd
from pathlib import Path, PurePath

import re

base_path = "/mnt/c/Users/CEEL-PC-005/Desktop/Joon/Final_scripts/Cancer_genes_analysis_of_APOBEC_motifs_test/" # CHANGE HERE

cdur_file = PurePath(base_path, "cdur.gencode.vM33.pc_transcripts.nopary.cdsonly.refseq.tc.csv")
cancer_genes_file = PurePath(base_path, "mouse_cancer_genes.txt")
control_genes_file = PurePath(base_path, "mouse_control_genes.txt")

cdur = pd.read_csv(cdur_file)
cancer_genes = pd.read_csv(cancer_genes_file, header=None)
control_genes = pd.read_csv(control_genes_file, header=None)

gene_class = []
for i in range(len(cdur["Transcript_name"].to_list())):
    id = cdur.iloc[i]["Ensembl_transcript_id"].split(".")[0]
    if id in control_genes[0].to_list():
        gene_class.append("control")
    elif id in cancer_genes[0].to_list():
        gene_class.append("cancer")
    else:
        gene_class.append("regular")

cdur["gene_class"] = gene_class

output_file = PurePath(base_path, "cdur.gencode.vM33.pc_transcripts.nopary.cdsonly.refseq.tc.geneclass.csv")
cdur.to_csv(output_file, index=False, sep="\t")

"""
#Ensembl_transcript_id
gene_class = []
for i in range(len(cdur["Transcript_name"].to_list())):
    if cdur.iloc[i in index_lst:
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
"""

