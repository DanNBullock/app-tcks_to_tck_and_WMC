
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 16:03:39 2022

@author: dan
"""
import nibabel as nib
import os
import sys

sys.path.append('wma_pyTools')
startDir=os.getcwd()
#some how set a path to wma pyTools repo directory
#wmaToolsDir='../wma_pyTools'
#wmaToolsDir='..'
import os
#os.chdir(wmaToolsDir)
print(os.getcwd())
print(os.listdir())
import wmaPyTools.roiTools
import wmaPyTools.analysisTools
import wmaPyTools.segmentationTools
import wmaPyTools.streamlineTools
import wmaPyTools.visTools
import numpy as np
import dipy.io.streamline
import dipy.tracking.utils as ut
#os.chdir(startDir)

import re
import subprocess
import os
import json
import pandas as pd
import nibabel as nib
from nilearn.image import resample_to_img
from glob import glob
from dipy.io.streamline import load_tractogram, save_tractogram

# load inputs from config.json
with open('config.json') as config_json:
	config = json.load(config_json)

#get the tract file paths
tcksToMerge=glob(os.path.join(config['tcks'],'*.tck'))
#get the names themselves
tckNames=[os.path.split(itcks)[1].replace('.tck','')  for itcks in tcksToMerge]

outStatefulTractogram, wmc_Dict=wmaPyTools.streamlineTools.inputTcks_to_WMCandTCK(tcksToMerge,names=tckNames)

if not os.path.exists(os.path.join('tck')):
    os.makedirs(os.path.join('tck'))
    save_tractogram(outStatefulTractogram,os.path.join('track.tck'), bbox_valid_check=False)

from scipy.io import savemat
#save down the classification structure
if not os.path.exists(os.path.join('wmc')):
    os.makedirs(os.path.join('wmc'))
    #savemat acts weird
savemat(os.path.join('wmc','classification.mat'),{ "classification": {"names": wmc_Dict['names'], "index": wmc_Dict['index'] }})
 

