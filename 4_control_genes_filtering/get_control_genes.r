library(biomaRt)

base_path <- "C:/Users/CEEL-PC-005/Desktop/Joon/Final_scripts/Cancer_genes_analysis_of_APOBEC_motifs_test/"

# get biomart from GRCh38 and 37
mart37 <- useEnsembl(biomart="ensembl", dataset = "hsapiens_gene_ensembl", GRCh=37)
mart38 <- useEnsembl(biomart="ensembl", dataset = "hsapiens_gene_ensembl")

# import preprocessed COSMIC point mutation and NCBI genes
cosmic_mutation_file <- paste(base_path, "CosmicMutantExport_genename_id_sorted_uniq.tsv", sep = "")   
genename_id <- read.csv(cosmic_mutation_file, header = FALSE, sep = "\t")

ncbi_human_file <- paste(base_path, "ncbi_human_clean.tsv", sep = "")
ncbi_human <- read.csv(ncbi_human_file, header = TRUE, sep = "\t")

# extract gene names and ids
genenames <- as.vector(genename_id$V1)
id_versions <- as.vector(genename_id$V2)

ids <- c()
for (i in 1:length(id_versions)){
  ids <- c(ids, strsplit(id_versions[i], "\\.")[[1]][1])
}

# set attributes to check
attributes.of.interest = c(
  "external_gene_name",
  "ensembl_transcript_id_version",
  "ensembl_transcript_id",
  "ensembl_gene_id",
  "chromosome_name",
  "start_position",
  "end_position"
)