#! /bin/bash

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/ceel/miniconda3/envs/cdur/lib
export CFLAGS="-I/home/ceel/miniconda3/envs/cdur/include"
export LDFLAGS="-L/home/ceel/miniconda3/envs/cdur/lib"

BASE_PATH="/mnt/c/Users/CEEL-PC-005/Desktop/Joon/Final_scripts/Cancer_genes_analysis_of_APOBEC_motifs_test/"
CDUR_PATH="/mnt/c/Users/CEEL-PC-005/Desktop/programs/CDUR"

mkdir ${BASE_PATH}cdur_palecto_run1-1 ${BASE_PATH}cdur_palecto_run2-1 ${BASE_PATH}cdur_palecto_run3-1

nohup python3 $CDUR_PATH/CDUR.py -i ${BASE_PATH}pteropus_alecto_pc_transcripts_part18.fa -m ./motif.txt -o ${BASE_PATH}cdur_palecto_run1-1/ -d 1 &> refseq_run1.log &
nohup python3 $CDUR_PATH/CDUR.py -i ${BASE_PATH}pteropus_alecto_pc_transcripts_part18.fa -m ./motif.txt -o ${BASE_PATH}cdur_palecto_run2-1/ -d 1 &> refseq_run2.log &
nohup python3 $CDUR_PATH/CDUR.py -i ${BASE_PATH}pteropus_alecto_pc_transcripts_part18.fa -m ./motif.txt -o ${BASE_PATH}cdur_palecto_run3-1/ -d 1 &> refseq_run3.log &

