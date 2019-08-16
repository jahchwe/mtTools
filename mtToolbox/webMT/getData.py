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
    study_name = studyPath.split('/')[1]

    #add study name to destination
    destination = os.path.join(os.path.expanduser(destination), study_name)
    if not os.path.exists(destination):
        os.mkdir(destination)
    
    #check if study exists
    try:
        ftp.cwd(study_path_server)
    except: 
        print("\nStudy not found. Please make sure path specified includes type and specific study name. \nFor example, a ratings study with the name of emotionReg would be specified as ratings/emotionReg/.\n")
        return
    #ftp.cwd("responses/" + studyPath + "/" + response_folders[studyPath.split("/")[0]])
    
    #check if directory exists at destination location
    #if not, create
        
    #list folders in a study
    folders = ftp.nlst()
    print(folders)

    for folder in folders:
        if '.' in folder:
            continue
    
        #ftp.cwd(os.path.join(study_path_server, folder))
        ftp.cwd(folder)

        #make destination folder
        if not os.path.exists(os.path.join(destination, folder)):
            os.mkdir(os.path.join(destination, folder))

        #list files in a folder
        files = ftp.nlst()

        for file in files:
            if "final" not in file:
                continue
            filename = os.path.join(destination, *[folder, file])
            try:
                with open(filename, "wb") as write_file:
                    print(filename)
                    ftp.retrbinary('RETR ' + file, write_file.write)

            except:
                pass
        ftp.cwd('..')
        #ftp.nlst pulls some file names that aren't strings

    
    



