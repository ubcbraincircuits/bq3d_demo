# -*- coding: utf-8 -*-
"""
script to set up the parameters for the image processing pipeline
"""
import os
from pathlib import Path

######################### Data parameters

#Directory to save all the results, usually containing the data for one sample
WorkingDirectory = str(Path('/Users/ytcao/Documents/GitHub/bq3d_demo/lifecanvas')) ###NOTE: from 01_bq3d_tutorial.ipynb step 1
AnalysisDirectory = str(Path(WorkingDirectory, "analysis"))
DataDirectory = str(Path(WorkingDirectory, "data"))

#Data File and Reference channel File, usually as a sequence of files from the microscope
AutofluoFile = str(Path(DataDirectory, '787287_NN_left_hemi_grayscale', "NN_428180_463220_025000_left_T\d{3,4}_Z405_C01.tif")) ###NOTE: from 01_bq3d_tutorial.ipynb step 2
SignalFile = str(Path(DataDirectory, '787287_cfos_left_hemi_grayscale', "787287_428180_463220_025000_full_sagittal_left_T\d{3,4}_Z410_C01.tif")) ###NOTE: from 01_bq3d_tutorial.ipynb step 2

#Resolution of the Raw Data (in um / pixel)
OriginalResolution = (9, 9, 9);

#Orientation: 1,2,3 means the same orientation as the reference and atlas files.
#Flip axis with - sign (eg. (-1,2,3) flips z). 3D Rotate by swapping numbers. (eg. (2,1,3) swaps x and y)
FinalOrientation = (1, -2, 3); #Left hemisphere orientation used
#FinalOrientation = (-1, -2, 3); #Right hemisphere orientation used

#Resolution of the Atlas (in um / pixel)
AtlasResolution = (25, 25, 25);
#Resolution to downsample to for correction between channels (in um/ pixel)
#We set AtlasResolution = CorrectionResolution to minimize blank areas appearing in atlas alignment for our data
CorrectionResolution =  (25, 25, 25);

#Path to registration parameters and atlases
PathReg = str(Path('/Users/ytcao/Documents/Warping')); ###NOTE: from 00_bq3d_setup.ipynb step 01_bq3d_tutorial.ipynb step 4
AtlasFile      = str(Path(PathReg, 'ARA2', 'average_template_25_right.tif'));
AnnotationFile = str(Path(PathReg, 'ARA2', 'annotation_25_right.tif'));

#Files to save cell info too.
# Coordinates and properties will be saved to this file
OutputProperties = ['centroid', 'sum', 'area']
sink = os.path.join(AnalysisDirectory, 'cells.json')

# File to save coordinates too after transforming to atlas
transformedCellsFile = os.path.join(AnalysisDirectory, 'cells_transformed.json')

######################### Cell Detection Parameters
# flow is a series of dictionaries containing which filters to run; must be a list (not a tuple)

flow = [
    {
        'filter'             : 'PixelClassification', #NOTE: This uses an ilastik Pixel Classification filter
        'size'          	 : 5,
        "save"               : os.path.join(AnalysisDirectory, 'bkgrdsub/Z\d{4}.tif'),
    },
    {
        'filter'             : 'Label',
        'mode'               : 1,
        'min_size'           : 3,
        'max_size'           : 50,
        'min_size2'          : 3,
        'max_size2'          : 50,
        'high_threshold'     : 0.30, #NOTE: probability threshold of 0.30 was optimal for our data
        'low_threshold'      : 450,
        "save"               : os.path.join(AnalysisDirectory, 'labels/Z\d{4}.tif'),
    }
]

CellDetectionParams = {
    # Specify the cropped range for the cell detection. If None will not crop.
    # This doesn't affect the resampling and registration operations
    'x' : None,
    'y' : None,
    'z' : None,

    # chunking args.
    #'processes'    : 1,           # number of physical cores to use, will override config value
    'min_sizes'    : (30,30,30),  # min substack size along each axis in pixels
    'overlap'      : 10,          # amount of overlap in pixels between substacks
    'aspect_ratio' : (1,10,10),   # ratio bewtween axes to maintain in substacks

    # general args. These do not normally need to be modified.
    'source'            : SignalFile,
    'flow'              : flow,
    'sink'              : sink,
    'output_properties' : OutputProperties,
    'log_level'         : 'verbose', # how much info to log in console
}

######################### Registration and Resampling Parameters
# These generally do not need to be modified

CorrectionResamplingParamSignal = {
    'interpolation'     : 'area',
    'source'            : SignalFile,
    'sink'              : os.path.join(AnalysisDirectory, 'signal_resampled_12.tif'),
    'resolutionSource'  : OriginalResolution,
    'resolutionSink'    : CorrectionResolution,
    'orientation'       : FinalOrientation,
}

CorrectionResamplingParamAuto = {
    **CorrectionResamplingParamSignal,
    'source'            : AutofluoFile,
    'sink'              : os.path.join(AnalysisDirectory, 'autofluo_resampled_12.tif'),
}

RegistrationResamplingParamSignal = {
    'interpolation'     : 'area',
    'source'            : SignalFile,
    'sink'              : os.path.join(AnalysisDirectory, 'signal_resampled_25.tif'),
    'resolutionSource'  : OriginalResolution,
    'resolutionSink'    : AtlasResolution,
    'orientation'       : FinalOrientation,
}

RegistrationResamplingParamAuto = {
    **RegistrationResamplingParamSignal,
    'source'            : AutofluoFile,
    'sink'              : os.path.join(AnalysisDirectory, 'autofluo_resampled_25.tif'),
}

CorrectionAlignmentParam = {
    #moving and reference images
    "fixedImage"   : CorrectionResamplingParamAuto["sink"],
    "movingImage"  : CorrectionResamplingParamSignal["sink"],

    #ants parameter files for alignment. see ants docs for definitions
    'type_of_transform' : 'Affine',
    'reg_iterations'    : (320,320,160,0),
    'aff_sampling'      : 256,

    #directory of the alignment result
    "resultDirectory" :  os.path.join(AnalysisDirectory, 'ants_signal_to_auto')
    }

RegistrationAlignmentParam = {
    #moving and reference images
    "fixedImage"   : AtlasFile,
    "movingImage"  : RegistrationResamplingParamAuto["sink"],

    #ants parameter files for alignment. see ants docs for definitions
    #NOTE: We used a more simple transform to minimize blank areas appearing in the atlas alignment
    'type_of_transform' : 'Affine',
    'reg_iterations'    : (320,320,160,0),
    'aff_sampling'      : 256,

    #directory of the alignment result
    "resultDirectory" :  os.path.join(AnalysisDirectory, 'ants_auto_to_atlas')
    }

#################### Heat map generation
# These generally do not need to be modified

voxelizeParameter = {
    "method" : 'Spherical', # Spherical,'Rectangular, Gaussian'
    "size" : (3, 3, 3) # Define size of each voxelized point in pixels
};

######################### Detected Cells Transformation Parameters
# transform coordinates from original positions to the atlas
# These generally do not need to be modified

CorrectionResamplingPointsParam = {
    'dataSizeSource'    : SignalFile,
    'resolutionSource'  : OriginalResolution,
    'resolutionSink'    : CorrectionResolution,
    'orientation'       : FinalOrientation,
}

CorrectionResamplingPointsInverseParam = {
    'dataSizeSource'    : CorrectionResamplingParamAuto['sink'],
    'dataSizeSink'      : SignalFile,
    'resolutionSource'  : CorrectionResolution,
    'resolutionSink'    : OriginalResolution,
    'orientation'       : FinalOrientation
}

RegistrationResamplingPointParam = {
    **CorrectionResamplingPointsParam,
    'resolutionSink'    : AtlasResolution,
    'dataSizeSink'      : RegistrationResamplingParamAuto['sink']
}
