library(biomaRt)
library(dplyr)
library(stringr)

mouse_mart <- useEnsembl(biomart="ensembl", dataset = "mmusculus_gene_ensembl")

# set attributes to view
# you can see possible attributes using: listAttributes(mart38)
attributes.of.interest = c(
  "external_gene_name",
  "ensembl_transcript_id_version",
  "ensembl_transcript_id",
  "ensembl_gene_id",
  "description",
  "gene_biotype",
  "transcript_gencode_basic",
  "transcript_appris",
  "transcript_is_canonical",
  "refseq_mrna",
  "refseq_mrna_predicted"
)

# import name and id of genes from gencode (cleaned for valid sequence)
base_path <- "C:/Users/CEEL-PC-005/Desktop/Joon/Final_scripts/Cancer_genes_analysis_of_APOBEC_motifs_test/"
name_id_file <- paste(base_path, "mmusculus_cancer_genes.csv", sep="")
genename_id <- read.csv(name_id_file, sep = ",")
refseq_ids <- gsub("\\..*","",genename_id$Transcript.Accession)
refseq_ids

cleaned_refseq_ids <- c()
for (id in refseq_ids) {
  if (str_split(id, "_")[[1]][1]=="NM" | str_split(id, "_")[[1]][1]=="XM"){
    cleaned_refseq_ids <- c(cleaned_refseq_ids, id)
  }
}
length(refseq_ids)
length(cleaned_refseq_ids)

# retrieve information from biomart
rlt_nm <- getBM(
  attributes = attributes.of.interest,
  filters = "refseq_mrna",
  values = cleaned_refseq_ids,
  mart = mouse_mart
)

rlt_xm <- getBM(
  attributes = attributes.of.interest,
  filters = "refseq_mrna_predicted",
  values = cleaned_refseq_ids,
  mart = mouse_mart
)

# get ENSEMBL ID with refseq
rlt$ensembl_transcript_id
length(refseq_ids)
length(rlt_nm$external_gene_name)
length(rlt_xm$external_gene_name)

unique(rlt_nm$ensembl_transcript_id)
mouse_cancer_genes_file <- paste(base_path, "mouse_cancer_genes.txt", sep="")
write(unique(rlt_nm$ensembl_transcript_id), mouse_cancer_genes_file)
