#############################################################################
#Written by Arvind K Yadav                                                  #
#PMTPred is developed for the prediction of protein methyltransefarses      #
#Please cite PMTPred                                                        #
#For details refer: https://github.com/ArvindYadav7/PMTPred                 #
#############################################################################

import pandas as pd
import numpy as np
import warnings
import argparse
import pickle
import shutil
import csv
import os
from argparse import RawTextHelpFormatter
warnings.filterwarnings('ignore')

if __name__ == "__main__":
    print("""
         **************************************************************************
              *   _____    __  __   _______   _____                      _   *
              *  |  __ \  |  \/  | |__   __| |  __ \                    | |  *
              *  | |__) | | \  / |    | |    | |__) |  _ __    ___    __| |  *
              *  |  ___/  | |\/| |    | |    |  ___/  | '__|  / _ \  / _` |  *
              *  | |      | |  | |    | |    | |      | |    |  __/ | (_| |  *
              *  |_|      |_|  |_|    |_|    |_|      |_|     \___|  \__,_|  *
              *                                                              *
              *      PMTPred: Protein Methyltransferases Prediction Tool     *
         **************************************************************************
                          @ https://github.com/ArvindYadav7/PMTPred 
                """)

print(" ")
parser = argparse.ArgumentParser(description='Please provide following arguments to proceed',formatter_class=RawTextHelpFormatter) 

#######################Read Arguments from command ###################################

parser.add_argument("-i", "--input", type=str, required=True, help="Input File Name: protein sequence file in FASTA format")

# Parameter initialization or assigning variable for command level arguments
args = parser.parse_args()
file_name = args.input

print("Loading...\n")

#threshold
t = 0.50

########################## Result Display ###########################################

def display_result(ids,svm_probs):
    
    ids=ids.tolist()
    output_file=open("Output.csv","w+")
    id_class=dict(zip(ids,svm_probs))
    
    for key in id_class:
        if id_class[key]>=t:
            line=str(key)+","+"PMT"+","+str(id_class[key])+"\n"
            output_file.write(line)
        else:
            line=str(key)+","+"nonPMT"+","+str(id_class[key])+"\n"
            output_file.write(line)

    output_file.close()

############################## Result Prediction #######################################

def predict_CKSAAP():
   
    test=pd.read_csv("CKSAAP.csv").fillna(0)
    ids=test['#']
    test=test.drop('#',axis=1)

    with open ("CKSAAP_model.pkl", "rb") as f:
        model = pickle.load(f)
    svm_predictions = model.predict(test)
    svm_probs = model.predict_proba(test)[:, 1]
    display_result(ids,svm_probs)
    return 

############################# Input file Preparation #############################

def prepare_input_file():
    
    string=""
    fh=csv.reader(open("CKSAAP.tsv"),delimiter="\t")
    fh2=open("CKSAAP.csv","w+")
        
    first_line=next(fh)
    string=",".join(first_line)
    fh2.write(string+"\n")
    string=""   
    for line in fh:
        string=",".join(line)
        string=string+"\n"
        fh2.write(string)
        string=""
       
    fh2.close()
    predict_CKSAAP()
    return

############################ Feature Extraction ###############################################

def extractfeature(filename):

    path, fn = os.path.split(filename)
    loc=os.getcwd()
    loc=str(loc)
    loc=loc.replace("\\","/")
    locforcopy=loc+"/iFeature/examples"
    locforifeature=loc+"/iFeature/iFeature.py"
    shutil.copy(filename,locforcopy)

    command="python "+locforifeature+" --file "+locforcopy+"/"+str(fn)+" --type CKSAAP --out CKSAAP.tsv"
    os.system(command)
    prepare_input_file()
    return

#call the extract feature function
extractfeature(file_name)


############################ END #########################
