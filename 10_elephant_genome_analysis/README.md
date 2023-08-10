# Orthologs analysis

## Get the list of cancer genes' NCBI Gene ID from COSMIC cancer census
This step you will generate list of NCBI Gene ID from COSMIC cancer census previously downloaded.

```console
python3 get_cancer_genes_ncbi_id.py
```

## Get the list of control genes' NCBI Gene ID from previous step
This step you will generate list of NCBI Gene ID from control genes generated from previous step.

```console
python3 get_control_genes_ncbi_id.py
```

## Download orthologs using NCBI Dataset command line tools

```
./download_orthologs_cancer_genes.sh
./download_orthologs_control_genes.sh
```

## Get the list of genes that all 10 species have
```
python3 get_cancer_genes_with_all_species.py
python3 get_control_genes_with_all_species.py
```

## Retrieve CDS of the genes
File names ending with *cdur* download only CDS, and the files without it downloads CDS with extra 1 bp 5' and 3' ends, respectively.
```
python3 download_valid_seq_for_cancer_genes.py
python3 download_valid_seq_for_cancer_genes_cdur.py
python3 download_valid_seq_for_control_genes.py
python3 download_valid_seq_for_control_genes_cdur.py
```

## Extract only human genes for sequential mutation
```
python3 extract_human_cancer_genes_for_seq_mut.py
python3 extract_human_control_genes_for_seq_mut.py
```

## Run sequential mutations and fix sequence names for CDUR
```
python3 gen_traj_for_cancer_genes_human.py
python3 fix_name_for_cdur_cancer.py
python3 gen_traj_for_control_genes_human.py
python3 fix_name_for_cdur_control.py
```

## Combine sequences into one file per caterogy
```
python3 combine_all_cancer_genes_orthologs_fasta.py
python3 combine_all_control_genes_orthologs_fasta.py
python3 combine_all_human_cancer_genes_fasta.py
python3 combine_all_human_control_genes_fasta.py
```




