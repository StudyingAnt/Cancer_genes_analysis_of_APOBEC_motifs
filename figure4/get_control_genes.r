library(biomaRt)

mart37 <- useEnsembl(biomart="ensembl", dataset = "hsapiens_gene_ensembl", GRCh=37)
mart38 <- useEnsembl(biomart="ensembl", dataset = "hsapiens_gene_ensembl")