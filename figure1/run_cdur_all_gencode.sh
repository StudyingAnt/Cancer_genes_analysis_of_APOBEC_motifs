#! /bin/bash

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/ceel/miniconda3/envs/cdur/lib
export CFLAGS="-I/home/ceel/miniconda3/envs/cdur/include"
export LDFLAGS="-L/home/ceel/miniconda3/envs/cdur/lib"

BASE_PATH="/mnt/c/Users/CEEL-PC-005/Desktop/Joon/Final_scripts/Cancer_genes_analysis_of_APOBEC_motifs_test/"
CDUR_PATH="/mnt/c/Users/CEEL-PC-005/Desktop/programs/CDUR"

mkdir ${BASE_PATH}cdur_all_genecode_run1 ${BASE_PATH}cdur_all_genecode_run2 ${BASE_PATH}cdur_all_genecode_run3

nohup python3 $CDUR_PATH/CDUR.py -i ${BASE_PATH}gencode.v40.pc_transcripts.nopary.cdsonly.test.fa -o ${BASE_PATH}cdur_all_genecode_run1/ -d 1 &> run1.log &
nohup python3 $CDUR_PATH/CDUR.py -i ${BASE_PATH}gencode.v40.pc_transcripts.nopary.cdsonly.test.fa -o ${BASE_PATH}cdur_all_genecode_run2/ -d 1 &> run2.log &
nohup python3 $CDUR_PATH/CDUR.py -i ${BASE_PATH}gencode.v40.pc_transcripts.nopary.cdsonly.test.fa -o ${BASE_PATH}cdur_all_genecode_run3/ -d 1 &> run3.log &

