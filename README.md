# bq3d_demo
BrainQuant3D setup for the [Hands-on, Neural, Behavioural and Histological Data Analysis Workshop](https://can-acn.org/meeting-2024/satellite-events/hands-on-neural-behavioural-and-histological-data-analysis-workshop-can2024-satellite/) by the UBC Dynamic Brain Circuit Cluster as a part of [CAN 2024](https://can-acn.org/meeting-2024/) meeting.

# Setup
Create a folder on your computer called "bq3d-demo-ubc" in a convenient location (such as your downloads folder). You can store all of the downloaded information here.

To start, download all the files in this Github repository as a zip file. Unzip the file into the "bq3d-demo-ubc" folder.

# Downloading Data
All data used for this tutorial is located at https://osf.io/m347v/.

- Allen Brain Atlas Registration files are in the [Brain Registration](https://osf.io/bmpw5/) OSF component. 
  - Click "Warping.zip" and select "Download" to download it (477.9 MB zipped, 2.32 GB unzipped).
  - Rename this folder to "warping".
- Demo CFOS signal brain image slices are in the [787287_cfos_left_hemi_grayscale](https://osf.io/v6q3b/) OSF component. 
  - Click the "OSF Storage (Canada - Montreal)" tab underneath "787287_cfos_left_hemi_grayscale" in the file tree, and then select "Download as zip" to download all the files (78.6 MB).
  - Rename this folder to "signal".
- Demo background autofluorescence brain image slices are in the [787287_NN_left_hemi_grayscale](https://osf.io/wbf2h/) OSF component.
  - Click the "OSF Storage (Canada - Montreal)" tab underneath "787287_NN_left_hemi_grayscale" in the file tree, and then select "Download as zip" to download all the files (78.6 MB).
  - Rename this folder to "auto".
- the Ilastik filter used is in the [ilastik filter](https://osf.io/jckgr/) OSF component. 
  - Click "cfos_6h_nov2.ilp.zip" and select "Download" to download it (794.6 MB zipped, 2.75 GB unzipped).
  - Rename this file to "ilastik-filters".

Unzip any data as necessary and move the folders/files into the "bq3d-demo-ubc" folder.

# Windows Setup
To use BrainQuant3D on Windows, you must install Windows Subsystem for Linux (WSL): https://learn.microsoft.com/en-us/windows/wsl/install. This allows Windows users to use Linux applications and command-line tools. You can then run all of your commands using the WSL app.

# Setting up the Jupyter Notebooks
You may need to download these programs onto your computer:
1. git (for setting up BrainQuant3D as a package): https://git-scm.com/downloads
2. anaconda for isolating packages in its own Python environment): https://www.anaconda.com/download

To find where you downloaded these files
Then, open your command line (mac, linux) or anaconda prompt (windows) and execute these commands:
```
cd <path to directory where this notebook and the .yml file is in> #e.g. cd mnt/ssd
```
> Hints for finding filepaths: 
> - Ubuntu Linux: Ctrl+L > Ctrl+C for an open directory in Files
>   - or Right-click file/folder > "Properties" 
> - Mac: Option+Right-click file/folder > "Copy <file> as Pathname" 
> - Windows: Shift+Right-click file/folder > "Copy as Path" 
```
conda env create -f bq3d_env.yml
conda activate bq3d
pip install git+https://github.com/MehwishUBC/BrainQuant3D_cFos.git
```
Choose the newly created "bq3d" conda environment as the kernel to run these Jupyter Notebooks and code. To activate Jupyter Notebooks, run this in your command line/anaconda prompt:
```
jupyter notebook
```
Start with Jupyter Notebook 00_bq3d_setup.ipynb.
