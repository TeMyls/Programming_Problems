import requests as rq
import re
import time

def motif(file):
    with open(file,'r') as f:
        
        ORIG_IDs = f.readlines()
        #Processing the IDs from the file cutting off the unnessary data such as newlines and descriptive spaces
        IDs = [ID.split("_")[0] for ID in ORIG_IDs]
        IDs = [ID.split()[0] for ID in IDs]
        #getting the text from the URLs. This works because the page is a fasta file data and nothing else 
        address_text = [rq.get(f"https://rest.uniprot.org/uniprotkb/{ID}.fasta").text for ID in IDs]
        #conversion of raw fasta data into string data by splitting individual text into list and joining
        #leaving out the  '>' at beginning of the fasta
        string_data = ["".join(txt.split("\n")[1:]) for txt in address_text]
       
        
        indexes = {}
        for sequence in string_data:
            indexes.update({sequence:[]})
            for j in range(0,len(sequence) - 3):
                seq = sequence[j:j+4]
                if (seq[0] == "N") and (seq[2] == "S" or seq[2] == "T") and (seq[1] and seq[3] != "P"):
                    indexes[sequence].append(j+1)
                
        for i, v in enumerate(indexes.values()):
            if v != []:
                print(ORIG_IDs[i].strip())
                print(" ".join(map(str,v)))
            
motif("rosalind_mprt.txt")

