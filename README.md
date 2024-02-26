# bq3d_demo
BrainQuant3D setup for the Data Analysis Workshop May 2024

Ensure you have these downloaded on your computer:
1. git (for setting up BrainQuant3D as a package): https://git-scm.com/downloads
2. anaconda/miniconda (for isolating packages in its own Python environment): https://www.anaconda.com/download

Then, open your command line (mac, linux) or anaconda prompt (windows) and execute these commands:
```
cd <path to directory where this notebook and the .yml file is in> #e.g. cd mnt/ssd
conda env create -f bq3d_env.yml
source activate bq3d_env
pip install git+https://github.com/sunilgandhilab/brainquant3d.git
```
Choose the newly created "bq3d" conda environment as the kernel to run these Jupyter Notebooks and code. To activate Jupyter Notebooks, run this in your command line/anaconda prompt:
```
jupyter notebook
```