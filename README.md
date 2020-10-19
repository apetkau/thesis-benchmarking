# Setup

```bash
git clone --recursive ...

conda create --name thesis-benchmarking --file environment.yml
conda activate environment.yml

pip install -e lib/cmdbench/
pip install aciitable
```

## Install extra tools

### Snippy

Some of the tools in the main conda environment appear to be incompatible with newer snippy versions (`4.6.0`) so you will have to install to a separate environment.

```bash
conda create --name snippy snippy
```

### Mentalist

```
conda create --name mentalist mentalist
```

### SnapperDB

#### Conda dependencies

```
# Can only use Python 2 and pip <= 9.0.3 due to installation issue
conda create --name snapperdb pip==9.0.3 python=2.7 numpy bwa bowtie2 samtools bcftools gatk picard
conda activate snapperdb
pip install phenix

# Install Python package from GitHub source
pip install -e lib/snapperdb
```

#### Finish installing GATK

Download GATK 3.8.1 from https://software.broadinstitute.org/gatk/download/archive.

```
cd lib/
tar -xvf package-archive_gatk_GenomeAnalysisTK-3.8-1-0-gf15c1c3ef.tar.bz2
gatk3-register $PWD/GenomeAnalysisTK-3.8-1-0-gf15c1c3ef/GenomeAnalysisTK.jar
```

#### Postgres

```
sudo apt install postgresql
```

# Datasets

I used data from <https://github.com/WGS-standards-and-analysis/datasets>. To download please do the following:

```bash
conda env create -f datasets-env.yml
conda activate wgs-standards-and-analysis

# I found checksums failed for the Genbank file, which I assume is because a new version was uploaded. You may need to modify the sha256 checksum in the Makefile if this error occurs.
GenFSGopher.pl --outdir Salmonella_enterica_1203NYJAP-1.simulated --layout byformat --numcpus 8 datasets/Salmonella_enterica_1203NYJAP-1.simulated.tsv

# For these files I found the reference tree was not available and so I had to remove the `tree.dnd` task from the Makefile.
GenFSGopher.pl --outdir Campylobacter_jejuni_0810PADBR-1 --layout byformat --numcpus 8 datasets/Campylobacter_jejuni_0810PADBR-1.tsv

# For these files the reference tree was not found (so I had to delete the `tree.dnd` task). And the genbank file sha256 code was different, so I updated it in the Makefile.
GenFSGopher.pl --outdir Escherichia_coli_1405WAEXK-1 --layout byformat --numcpus 8 datasets/Escherichia_coli_1405WAEXK-
1.tsv
```
