#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 15:26:28 2018

@author: jahchwe

mtTools

instructions on subparsers: https://stackoverflow.com/questions/9505898/conditional-command-line-arguments-in-python-using-argparse

"""

from mtToolbox.webMT.getData import getData
from mtToolbox.webMT.concatResponses import concatResponses
import argparse


def selectFunction(args):
    if args.command == "getData":
        getData(args.password, args.studyPath, args.destination)
    
    elif args.command == "concatResponses":
        concatResponses(args.dataPath, args.outputFilename)
    
        

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Tools to complement webMT. <:3)~")
    #selection of function
    
    subparsers = parser.add_subparsers(
            title = "Functions",
            description = "Type -h for more help on any given function.",
            dest = "command")
    #subparsers per selection
    
    #for getData
    parser_getData = subparsers.add_parser(
            "getData",
            help = "Retrieves data from server and stores at specified path.")
    
    parser_getData.add_argument(
            "password", 
            help = "Password for server. <8^)")
    parser_getData.add_argument(
            "studyPath",
            help = "Path of responses. Needs to be csv. Include the type of study in the path. Types of studies supported: ratings, mt, decisionTask, and rc. For example, a ratings study with the name of emotionReg would be specified as ratings/emotionReg/ratings.")
    parser_getData.add_argument(
            "destination",
            help = "Local destination path for data.")
    
    #for concatResponses
    parser_concat = subparsers.add_parser(
            "concatResponses",
            help = "Concatenates raw webMT data into one file. Only concatenates final files. NOTE: Does not work for .mt files, only csv.")
    
    
    parser_concat.add_argument(
            "dataPath",
            help = "Local path to raw webMT data.")
    parser_concat.add_argument(
            "outputFilename",
            help = "Name of output file. Will be placed in directory with raw data.")
    '''
    parser_concat.add_argument(
            "--descriptives",
            help = "Run descriptives on data.",
            action = "store_true")
    '''
    
    args = parser.parse_args()
    selectFunction(args)
    

