#jayShreeRam
#PMTPred

file_name = "InputSequences.fasta"

#threshold
t = 0.50

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
    
def predict_CKSAAP():
    import pandas as pd
    import pickle
    import numpy as np
   
    test=pd.read_csv("CKSAAP.csv").fillna(0)
    ids=test['#']
    test=test.drop('#',axis=1)

    with open ("CKSAAP_model.pkl", "rb") as f:
        model = pickle.load(f)
    svm_predictions = model.predict(test)
    svm_probs = model.predict_proba(test)[:, 1]
    display_result(ids,svm_probs)
    return 

def prepare_input_file():
    string=""
    import csv
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

def extractfeature(filename):
    import os
    import shutil
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
