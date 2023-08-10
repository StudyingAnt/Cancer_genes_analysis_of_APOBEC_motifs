from pathlib import Path, PurePath
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

seq_records = []

base_path = Path("/mnt/c/Users/CEEL-PC-005/Desktop/Joon/Final_scripts/Cancer_genes_analysis_of_APOBEC_motifs_test/caenorhabditis_elegans_genes/")
save_path = "/mnt/c/Users/CEEL-PC-005/Desktop/Joon/Final_scripts/Cancer_genes_analysis_of_APOBEC_motifs_test/"

seq_records = []
i = 0
for cnt, file in enumerate(base_path.iterdir()):
    if file.is_file():
        prev_i = i
        i = cnt//3570
        print(f"{cnt}")
        if i > prev_i:
            output_file = PurePath(save_path, f"caenorhabditis_elegans_pc_transcripts_part{prev_i}.fa")
            SeqIO.write(seq_records, output_file, "fasta")
            seq_records = []
            seq_records.append(list(SeqIO.parse(file, "fasta"))[0])
        else:
            seq_records.append(list(SeqIO.parse(file, "fasta"))[0])


output_file = PurePath(save_path, f"caenorhabditis_elegans_pc_transcripts_part{prev_i}.fa")
SeqIO.write(seq_records, output_file, "fasta")





