# bq3d_demo
BrainQuant3D setup for the Data Analysis Workshop May 2024

# Downloading Data
All data used for this tutorial is located at https://osf.io/m347v/?view_only=f0cc945410554286b78c10e41ab511bb.

- Allen Brain Atlas Registration files are in the "Brain Registration" OSF component. Click the file and select "Check out file" to download it (477.9 MB zipped, 2.32 GB unzipped).
- Demo brain image slices are in the "Demo Data Subset" OSF component. Press the "OSF Storage (Canada - Montreal)" tab underneath "Demo Data Subset" in the file tree, and then select "Download as zip" to unwrap all the files (78.6 MB).
- the Ilastik filter used is in the "ilastik filter" OSF component. Click the file and select "Check out file" to download it (794.6 MB zipped, 2.75 GB unzipped).

# Setting up the Jupyter Notebooks
You may need to download these programs onto your computer:
1. git (for setting up BrainQuant3D as a package): https://git-scm.com/downloads
2. anaconda for isolating packages in its own Python environment): https://www.anaconda.com/download

To find where you downloaded these files
Then, open your command line (mac, linux) or anaconda prompt (windows) and execute these commands:
```
cd <path to directory where this notebook and the .yml file is in> #e.g. cd mnt/ssd
conda env create -f bq3d_env.yml
conda activate bq3d
pip install git+https://github.com/sunilgandhilab/brainquant3d.git
```
Choose the newly created "bq3d" conda environment as the kernel to run these Jupyter Notebooks and code. To activate Jupyter Notebooks, run this in your command line/anaconda prompt:
```
jupyter notebook
```
Start with Jupyter Notebook 00_bq3d_setup.ipynb.
