## How to install CDUR
CDUR was developed before `Biopython 1.78`, and utilize `Bio.Alphabet` module now removed.
Here we provide a way to install CDUR in `conda` environment.

### Make `conda` envirionment
```console
conda create --name cdur python=3.6
conda activate cdur
```

### Clone CDUR
```console
git clone https://gitlab.com/maccarthyslab/CDUR.git
```

### Install required package
```console
conda install -c conda-forge gsl --yes
conda install -c conda-forge numpy --yes
conda install -c conda-forge scipy --yes
conda install -c conda-forge pandas --yes
conda install -c conda-forge biopython=1.77 –yes
```

### Change makefile
Add `-I$${HOME}/miniconda3/envs/cdur/include -L$${HOME}/miniconda3/envs/cdur/lib` before `-o` option.

**Original**
```Makefile
all:
	g++ -O3 HotspotStatisticsReporter.cpp util.cpp StateVector.cpp Sequence.cpp Mutation.cpp scharff_utils.cpp ContinuousHistogram.cpp GeneticCode.cpp DiscreteHistogram.cpp MotifReference.cpp MotifIdentifier.cpp Motif.cpp EgnetProperties.cpp FrequencyDependentRandomizer.cpp Properties.cpp SequenceDataset.cpp StatsSampler.cpp BivariateNormalConditional.cpp generate.cpp analysis.cpp MotifMutationPair.cpp MotifMutationFrequency.cpp StatsSampler2Vars.cpp SimpleFastaReader.cpp RandomizedIota.cpp -I./ -I./tnt -o shmsim -lgsl -lgslcblas -lm -O

```
**Modified**
```Makefile
all:
	g++ -O3 HotspotStatisticsReporter.cpp util.cpp StateVector.cpp Sequence.cpp Mutation.cpp scharff_utils.cpp ContinuousHistogram.cpp GeneticCode.cpp DiscreteHistogram.cpp MotifReference.cpp MotifIdentifier.cpp Motif.cpp EgnetProperties.cpp FrequencyDependentRandomizer.cpp Properties.cpp SequenceDataset.cpp StatsSampler.cpp BivariateNormalConditional.cpp generate.cpp analysis.cpp MotifMutationPair.cpp MotifMutationFrequency.cpp StatsSampler2Vars.cpp SimpleFastaReader.cpp RandomizedIota.cpp -I./ -I./tnt -I$${HOME}/miniconda3/envs/cdur/include -L$${HOME}/miniconda3/envs/cdur/lib -o shmsim -lgsl -lgslcblas -lm -O

```
### Modify CDUR.py
From line 362, please modify original code as following to use `-o` and `-d` option.

**Original**
```Python
    if args.motifs is not None:
        os.system("~/CDUR/shmsim "+args.out_folder + seq_name[1:-1]+'_'+args.random_type+'.fasta ' + args.motifs + ' > ' + args.out_folder + seq_name[1:-1] + '_' + args.random_type + 'results.txt')

        if args.delete:
            try:
                os.remove(args.out_folder + seq_name[1:-1]+'.fas')
            except Exception:
                pass

            try:
                os.remove(f"{args.out_folder}{seq_name[1:-1]}_{args.random_type}.fasta")
            except Exception:
                pass
    else:
	    os.system("~/CDUR/shmsim "+seq_name[1:-1]+'_'+args.random_type+'.fasta > ' + seq_name[1:-1] + '_' + args.random_type + 'results.txt')

```

**Modified**
```Python
    if args.motifs is not None:
        os.system("~/CDUR/shmsim "+args.out_folder + seq_name[1:-1]+'_'+args.random_type+'.fasta ' + args.motifs + ' > ' + args.out_folder + seq_name[1:-1] + '_' + args.random_type + 'results.txt')

        if args.delete:
            try:
                os.remove(args.out_folder + seq_name[1:-1]+'.fas')
            except Exception:
                pass

            try:
                os.remove(f"{args.out_folder}{seq_name[1:-1]}_{args.random_type}.fasta")
            except Exception:
                pass
    else:
        os.system("~/CDUR/shmsim "+args.out_folder + seq_name[1:-1]+'_'+args.random_type+'.fasta > ' + args.out_folder + seq_name[1:-1] + '_' + args.random_type + 'results.txt')

        if args.delete:
            try:
                os.remove(args.out_folder + seq_name[1:-1]+'.fas')
            except Exception:
                pass

            try:
                os.remove(f"{args.out_folder}{seq_name[1:-1]}_{args.random_type}.fasta")
            except Exception:
                pass
```

Run following command in terminal to set `shmsim` location.

```console
PATH_TO_CDUR=/path/to/cdur/you/have/
sed -i "s+~/CDUR/shmsim+${PATH_TO_CDUR}/shmsim+g" ${PATH_TO_CDUR}/CDUR.py
```

## Run CDUR to all transcripts
```console
./run_cdur_all_gencode.sh
```