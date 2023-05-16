## How to install CDUR
CDUR was developed before `Biopython 1.78`, and utilize `Bio.Alphabet` module now removed.
Here we provide how to install CDUR in `conda` environment.

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
```Makefile
all:
	g++ -O3 HotspotStatisticsReporter.cpp util.cpp StateVector.cpp Sequence.cpp Mutation.cpp scharff_utils.cpp ContinuousHistogram.cpp GeneticCode.cpp DiscreteHistogram.cpp MotifReference.cpp MotifIdentifier.cpp Motif.cpp EgnetProperties.cpp FrequencyDependentRandomizer.cpp Properties.cpp SequenceDataset.cpp StatsSampler.cpp BivariateNormalConditional.cpp generate.cpp analysis.cpp MotifMutationPair.cpp MotifMutationFrequency.cpp StatsSampler2Vars.cpp SimpleFastaReader.cpp RandomizedIota.cpp -I./ -I./tnt -I$${HOME}/miniconda3/envs/cdur/include -L$${HOME}/miniconda3/envs/cdur/lib -o shmsim -lgsl -lgslcblas -lm -O

```
