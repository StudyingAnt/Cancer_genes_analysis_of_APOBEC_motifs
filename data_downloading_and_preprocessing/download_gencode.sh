#! /bin/bash

DOWNLOAD_PATH="/path/to/download" # CHANGE HERE

release_num=40

# download and unzip data
wget -P ${DOWNLOAD_PATH} http://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_${release_num}/gencode.v${release_num}.pc_transcripts.fa.gz
gunzip -c ${DOWNLOAD_PATH}gencode.v${release_num}.pc_transcripts.fa.gz > ${PROJECT_PATH}/exp/${EXP_NAME}/in/gencode.v${release_num}.pc_transcripts.fa
