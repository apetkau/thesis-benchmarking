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
pip install snapperdb phenix
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
