# import package
library(dplyr)

base_path <- "C:/Users/CEEL-PC-005/Desktop/Joon/Final_scripts/Cancer_genes_analysis_of_APOBEC_motifs_test/"
cdur_file <- paste(base_path, "cdur.gencode.vM33.pc_transcripts.nopary.cdsonly.refseq.tc.csv", sep = "")
cdur_data <- read.table(file = cdur_file,  sep = ',', header = TRUE)

# for gene ontology analysis
get_genename <- function(str) { 
  if (substring(str, 1, 4) == "ENS") {
    return(str)
  } else {
    return (substring(str, 1, nchar(str)-4))  
  }
  
}

# filter left-top
left_top <- cdur_data %>% 
  filter(Motif_under.representation <= 0.05) %>% 
  filter(Mutational_susceptibility <= 0.05)

left_top_file <- paste(base_path, "mouse_top_left.txt", sep="")
write(unique(unlist(lapply(left_top$Transcript_name, get_genename))), left_top_file)

# filter right-bottom
right_bottom <- cdur_data %>% 
  filter(Motif_under.representation >= 0.95) %>% 
  filter(Mutational_susceptibility >= 0.95)

right_bottom_file <- paste(base_path, "mouse_right_bottom.txt", sep="")
write(unique(unlist(lapply(right_bottom$Transcript_name, get_genename))), right_bottom_file)


length(unique(unlist(lapply(cdur_data$Transcript_name, get_genename))))
low_rep <- cdur_data %>% 
  filter(Motif_under.representation <= 0.05)
length(unique(unlist(lapply(low_rep$Transcript_name, get_genename))))
mid_rep <- cdur_data %>% 
  filter(Motif_under.representation > 0.05) %>% 
  filter(Motif_under.representation < 0.95)
length(unique(unlist(lapply(mid_rep$Transcript_name, get_genename))))
high_rep <- cdur_data %>% 
  filter(Motif_under.representation >= 0.95)
length(unique(unlist(lapply(high_rep$Transcript_name, get_genename))))
