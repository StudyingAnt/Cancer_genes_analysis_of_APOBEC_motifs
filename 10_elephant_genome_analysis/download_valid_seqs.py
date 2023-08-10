from pathlib import Path, PurePath
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

from Bio import Entrez

import pandas as pd
import time
import numpy as np

Entrez.email = "joon-hyun.song@stonybrook.edu"

# directory to input and output files
base_path = "/mnt/c/Users/CEEL-PC-005/Desktop/Joon/Final_scripts/Cancer_genes_analysis_of_APOBEC_motifs_test/" # CHANGE HERE
ncbi_palecto_file = Path(PurePath(base_path, "ncbi_palecto_clean.tsv"))


ncbi_palecto = pd.read_csv(ncbi_palecto_file, sep="\t")

seq_records = []
for idx, gene_id in enumerate(ncbi_palecto["gene_id"].to_list()):
    if ncbi_palecto.iloc[idx]["type"] == "PROTEIN_CODING" and idx > 630:
        time.sleep(3*np.random.rand())
        handle = Entrez.efetch(db="gene", id=gene_id, rettype="gb", retmode="xml")
        record = Entrez.read(handle)
        handle.close()

        gene_name = record[0]["Entrezgene_gene"]["Gene-ref"]['Gene-ref_desc']
        gene_symbol = record[0]["Entrezgene_gene"]["Gene-ref"]['Gene-ref_locus']
        #print(f"{gene_id}\tPROTEIN_CODING\t{gene_symbol}")

        for product in record[0]["Entrezgene_locus"][0]["Gene-commentary_products"]:
            time.sleep(3*np.random.rand())
            if 'Gene-commentary_label' in product.keys():
                transcript_variant = product['Gene-commentary_label']
            else:
                transcript_variant = ""

            #print(product['Gene-commentary_accession'])
            ref_id = product['Gene-commentary_accession']

            if ref_id[1] != "R":
                subhandle = Entrez.efetch(db="nucleotide", id=ref_id, rettype="gb", retmode="xml")
                subrecord = Entrez.read(subhandle)
                subhandle.close()

                cds_indices = []
                for i in range(len(subrecord[0]["GBSeq_feature-table"])):
                    for key, value in subrecord[0]["GBSeq_feature-table"][i].items():
                        if key == "GBFeature_key" and value == "CDS":
                            cds_indices.append(i)

                froms = []
                tos = []
                for i in cds_indices:
                    for key, value in subrecord[0]["GBSeq_feature-table"][i].items():
                        if key == "GBFeature_intervals":
                            froms.append(int(value[0]["GBInterval_from"]))
                            tos.append(int(value[0]["GBInterval_to"]))

                from_idx = froms[0]
                to_idx = tos[0]

                if transcript_variant:
                    new_id = f"{ref_id}_Pteropus_alecto_{gene_symbol}_{'_'.join(transcript_variant.split())}"
                else:
                    new_id = f"{ref_id}_Pteropus_alecto_{gene_symbol}"

                seq_record = SeqRecord(Seq(subrecord[0]["GBSeq_sequence"][from_idx-1:to_idx].upper()), id=new_id, description="")
                SeqIO.write(seq_record, PurePath(base_path, "pteropus_alecto_genes", f"{new_id}.fa"), "fasta")
                print(seq_record.id)
                #print(seq_record.seq)
                seq_records.append(seq_record)           

output_file = PurePath(base_path, f"pteropus_alecto_pc_transcripts.fa")
SeqIO.write(seq_records, output_file, "fasta")



"""
for path in cancer_genes_path.iterdir():
    if path.is_dir():
        genename = str(path).split("/")[-1]

        if genename in cancer_genes_having_ten_orthologs["Gene_name"].to_list(): 
            fasta_file = PurePath(path, "ncbi_dataset", "data", "gene.fna")
            infos_file = PurePath(path, "ncbi_dataset", "data", "transcript_protein.tsv")

            infos = pd.read_csv(infos_file, sep="\t")

            print(genename)
            seq_records = []
            for i, species in enumerate(species_of_interest):
                tmp_infos = infos[infos["Taxonomic Name"] == species]
                tmp_infos = tmp_infos[~tmp_infos["Transcript Protein Length"].isna()]

                # pick NM if exist
                if sum(tmp_infos["Transcript Accession"].str.match("^NM")):
                    tmp_infos = tmp_infos[tmp_infos["Transcript Accession"].str.match("^NM")]
                    tmp_infos = tmp_infos[["Taxonomic Name", "Transcript Accession", "Transcript Protein Length"]].sort_values("Transcript Protein Length", ascending=False)
                else:
                    tmp_infos = tmp_infos[["Taxonomic Name", "Transcript Accession", "Transcript Protein Length"]].sort_values("Transcript Protein Length", ascending=False)

                ref_id = tmp_infos.iloc[0]["Transcript Accession"]
                species_name = tmp_infos.iloc[0]["Taxonomic Name"]

                handle = Entrez.efetch(db="nucleotide", id=ref_id, rettype="gb", retmode="xml")
                record = Entrez.read(handle)
                handle.close()

                cds_indices = []
                for i in range(len(record[0]["GBSeq_feature-table"])):
                    for key, value in record[0]["GBSeq_feature-table"][i].items():
                        if key == "GBFeature_key" and value == "CDS":
                            cds_indices.append(i)

                froms = []
                tos = []
                for i in cds_indices:
                    for key, value in record[0]["GBSeq_feature-table"][i].items():
                        if key == "GBFeature_intervals":
                            froms.append(int(value[0]["GBInterval_from"]))
                            tos.append(int(value[0]["GBInterval_to"]))

                from_idx = froms[0]
                to_idx = tos[0]

                if record[0]["GBSeq_definition"].split()[0] == "PREDICTED:":
                    new_id = f"{'_'.join(record[0]['GBSeq_definition'].split()[1:3])}_{genename.lower()}"
                else:
                    new_id = f"{'_'.join(record[0]['GBSeq_definition'].split()[0:2])}_{genename.lower()}"

                if from_idx-2 > -1 and to_idx+1 <= int(record[0]["GBSeq_feature-table"][0]["GBFeature_intervals"][0]["GBInterval_to"]):
                    seq_record = SeqRecord(Seq(record[0]["GBSeq_sequence"][from_idx-2:to_idx+1].upper()), id=new_id, description="")
                    seq_records.append(seq_record)
                            
            output_file = PurePath(str(path), f"ten_species_{genename.lower()}.fa")
            SeqIO.write(seq_records, output_file, "fasta")
   
"""