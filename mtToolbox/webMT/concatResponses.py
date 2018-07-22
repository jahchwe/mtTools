#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 12:34:19 2018

@author: jahchwe

concatResponses
"""

import os
import pandas as pd
import glob

def concatResponses(dataPath, outputFilename):
    dataPath = os.path.expanduser(dataPath)
    files = glob.glob(dataPath + "/*.csv")
    #print(files)
    
    df = pd.concat([pd.read_csv(x) for x in files if x.split("/")[-1].startswith("final")])
    
    if outputFilename.endswith(".csv"):
        outputFilename = outputFilename[:-4]
    
    output_path = os.path.join(dataPath, outputFilename + ".csv")
    
    df.to_csv(output_path, index = False)
    

    

