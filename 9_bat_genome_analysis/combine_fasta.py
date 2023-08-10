from pathlib import Path, PurePath
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

seq_records = []

base_path = Path("/mnt/c/Users/CEEL-PC-005/Desktop/Joon/Final_scripts/Cancer_genes_analysis_of_APOBEC_motifs_test/pteropus_alecto_genes/")

seq_records = []
for file in base_path.iterdir():
    if file.is_file():
        seq_records.append(list(SeqIO.parse(file, "fasta"))[0])

base_path = "/mnt/c/Users/CEEL-PC-005/Desktop/Joon/Final_scripts/Cancer_genes_analysis_of_APOBEC_motifs_test/"

output_file = PurePath(base_path, f"pteropus_alecto_pc_transcripts.fa")
SeqIO.write(seq_records, output_file, "fasta")


