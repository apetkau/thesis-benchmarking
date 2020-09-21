# Setup

```bash
git clone --recursive ...

conda create --name thesis-benchmarking --file environment.yml
conda activate environment.yml

pip install -e lib/cmdbench/
pip install aciitable
```

## Install snippy

Some of the tools in the main conda environment appear to be incompatible with newer snippy versions (`4.6.0`) so you will have to install to a separate environment.

```bash
conda create --name snippy snippy
```
