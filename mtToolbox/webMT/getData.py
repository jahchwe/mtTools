#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 20:06:24 2018

@author: jahchwe

mtTools.py getData

"""

from ftplib import FTP, all_errors
import os

def getData(password, studyPath, destination):
    
    try: 
        ftp = FTP("jbfreeman.net", "webmt@jbfreeman.net", password)
    except all_errors as e:
        print(e)
        return
        
    #the folder name of responses depends on the type of study
    #split study path by / and get correct response folder name
    
    #response_folders = {"ratings": "ratings", "mt":"MT", "decisionTask": "decisionTask", "rc":"revcorr"}
    
    #handle if specified response path contains leading / or not
    if studyPath.split("/")[0] == "":
        studyPath = "/".join(studyPath.split("/")[1:])
    
    study_path_server = os.path.join("responses/", studyPath)
    
    #check if study exists
    try:
        ftp.cwd(study_path_server)
    except: 
        print("\nStudy not found. Please make sure path specified includes type and specific study name. \nFor example, a ratings study with the name of emotionReg would be specified as ratings/emotionReg/ratings.\n")
        return
    #ftp.cwd("responses/" + studyPath + "/" + response_folders[studyPath.split("/")[0]])
    
    #check if directory exists at destination location
    #if not, create
    
    store_path = os.path.expanduser(destination)
    
    if not os.path.exists(store_path):
        os.makedirs(store_path)
        
    #download files using stackoverflow link
    files = ftp.nlst()
    num_files = len(files)
    
    files_not_downloaded = []
    
    for counter, file in enumerate(files):
        filename = os.path.join(store_path, file)
        
        #ftp.nlst pulls some file names that aren't strings
        
        try: 
            with open(filename, "wb") as write_file: 
                ftp.retrbinary('RETR '+ file, write_file.write)
            print("%d/%d files downloaded." % (counter + 1 - len(files_not_downloaded), num_files))
    
        except:
            files_not_downloaded.append(file)
    
    if len(files_not_downloaded) != 0:
        print("All files downloaded except:")
        for file in files_not_downloaded:
            print(file, end = ", ")
        print("")
    else:
        print("All files downloaded!")
    
    



