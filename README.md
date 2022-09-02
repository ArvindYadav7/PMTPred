# PMTPred
A method for the prediction of protein methyltransferases (PMTs). To cater a wider usersbase, and contribute to the research community, we have provided this open source standalone tool PMTPred. 
# Introduction
PMTs constitute a class of enzymes that catalyze the methylation of lysine or arginine  residues on histones and non-histones proteins. A number of PMTs have been directly associated with the pathogenesis of diseases such as human cancers, inflammatory diseases, neurodegenerative diseases etc. 

PMTPred is a freely available standalone software package developed to predict the PMTs with high accuracy using SVM algorithm. This software could be used to fast and accurate prediction and large scale annotation project for the PMTs with high speed. It allows users to flexible use by providing protein sequence in fasta file as an input and this program will predict the class of given query protein sequence with prediction pprobability score.This page provides information about standalone PMTPred
# Requirement
This method is developed using platform of python version 3 (version 3.8). Before running PMTPred, user should make sure all the following packages are installed in their python environment. 
1. Numpy
2. Pandas
3. Pickle
4. Sklearn
# Download
1.	Download the repo using https://github.com/ArvindYadav7/PMTPred 
2.	Extract or uncompress the PMTPred-main.zip file.
3.	See how to use section to find instruction for running the program.
# How to use
1. Open the 'Command Prompt' on Windows OS by typing in search tool.
2. Navigate to your uncompressed PMTPred folder by ## cd /path/PMTPred
3. Run ## python PMTPred.py -h for for instructions regarding running of the program.
It will provide the complete list of options for usage.
## Full Usage
usage: 

# Input File
User must have the input fasta file of protein sequence. The fasta file may have one or more sequences in standard fasta format.
# Output File
Program will save result in CSV format, in case user do not provide output file name, it will be stored in Output.csv.
# Datasets
All datasets can be downloaded from: http://bioinfoindia.org/PMTPred/ 

