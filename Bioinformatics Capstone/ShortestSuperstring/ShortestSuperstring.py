import time
import random
from Bio import SeqIO
import statistics

string1 = "gctaagttcatgcatc"
arr = ["catg", "ctaagt", "gcta","atgcatc" ,"ttca"]

string2 = "acccgatatta"
arr2 = ["accc","cccgat","atatt","gattata"]

string3 = "AGAGTCATCCAGCTGGAGCCCTGAGTGGCTGAGCTCAGGC"
arr3 = [
    "AGAGTCATCCAGCTG",
    "TCCAGCTGGAGCCC",
    "TCCAGCTGGAGCCCTG",
    "CATCCAGCTGGAGCC",
    "CCTGAGTGGCTGAGCT",
    "TGGCTGAGCTCAGGC",
    "AGCCCTGAGTGGCTG",
    "GTCATCCAGCTGGA",
    "AGAGTCAT",
    "CCCTGAGTGG"
]

string4 = "gtcaagttcatgcatc"
arr4 = [string4[i:i+6] for i in range(len(string4)) if i + 6 < len(string4) + 1]

def combiner(string1,string2):
    ol_letters ,max_ol = "" ,0
    
    if len(string1) < len(string2):
        shorter = string1
        longer = string2
    elif len(string1) > len(string2):
        shorter = string2
        longer = string1
    else:
        shorter = string1
        longer = string2
        
    for i in range(len(longer)):
        #shorter's suffix to longer's prefix
        if i <= len(shorter):
            #checks if suffix of shorter overlaps with prefix of longer and records the longest overlap
            #print(shorter[len(shorter)-i:],longer[:i],sep='_')
            if shorter[-i:] == longer[:i]:
                if len(longer[:i]) > len(ol_letters):
                    ol_letters  = longer[:i]
                    max_ol = len(ol_letters)
        #sees if anything in longer matches up with shorter
        if i + len(shorter) <= len(longer) + 1:
            #print(shorter,longer[i:len(shorter) - 1 + i],sep= '*')
            if shorter == longer[i:len(shorter) - 1 + i]:
                if len(longer[:i]) > len(ol_letters):
                    ol_letters = longer[i:len(shorter) - 1 + i]
                    max_ol = len(ol_letters)
        #shorter's prefix to longer's suffix
        if i <= len(shorter):
            #sees if anything in longer matches up with shorter
            # print(shorter[:i],longer[len(longer)-i:],sep='|')
            if shorter[:i] == longer[-i:]:
                if len(shorter[:i]) > len(ol_letters):
                    ol_letters =  longer[len(longer)-i:]
                    max_ol = len(ol_letters)

    
    
    marker = longer.find(ol_letters)
    if marker > len(shorter):
        
        #print("test1")
        return longer, max_ol
    elif max_ol > 0:
        if len(shorter) == len(longer):
            #print("test2")
            #shorter's prefix to longer's suffix
            if shorter[:max_ol] == longer[len(longer)-max_ol:]:
                return longer + shorter[max_ol:] , max_ol
            #shorter's suffix to longer's prefix
            elif shorter[len(shorter)-max_ol:] == longer[:max_ol]:
                return shorter + longer[max_ol:], max_ol
        #prefix of one equals suffix for one character then combined at that point
        elif max_ol == 1:
            #print("test3")
            #shorter's prefix to longer's suffix
            if shorter[:1] == longer[len(longer) - 1:]:
                return  longer + shorter[1:], max_ol
            #shorter's suffix to longer's prefix
            elif shorter[len(shorter) - 1:] == longer[:1]:
                return shorter + longer[1:], max_ol
        #if shorter is part of a substring of longer,the overlapping region of substring longer is spliced and the remainder is added
        #to shorter or longer depending on the overlap
        else:
            #print("test4")
            
            #shorter's prefix to longer's suffix
            if shorter[:max_ol] == longer[len(longer) - max_ol:]:
                return longer + shorter[max_ol:], max_ol
            #shorter's suffix to longer's prefix
            if shorter[len(shorter) - max_ol:] == longer[:max_ol]:
                return shorter + longer[max_ol:], max_ol
    elif max_ol == 0:
        #print("test5")
        return shorter + longer, max_ol
        
def greedy_scs(arr):
    max_overlap, index_1,index_2,true_string = 0 ,0 ,0 ,""
    #print(len(arr))
    
    if len(arr) == 1:
        return arr[0]
    
    for j in range(1,len(arr)):
        string_overlap = combiner(arr[0],arr[j])
        string = string_overlap[0]
        overlap = string_overlap[1]
        #Making the overlap exceed a certain amount in order to
        #ensure biological relevant
        if overlap >= max_overlap and overlap > 8:
            max_overlap = overlap
            true_string = string
            index_1 = 0
            index_2 = j
            
    print(max_overlap)
    #removal from array has to be like this so the indexing doesn't mess up    
    if index_2 != 0:
        arr.pop(index_2)
        arr.pop(index_1)
        arr.append(true_string)
    else:
        arr.pop(index_1)
    
    
    
    
    
    return greedy_scs(arr)



def reader(file,limit):
    reads = []
    cnt = 0
    #note you only get half of the reads in limit
    with open(file,"r") as f:
        while True:
            cnt += 1
            line = f.readline().strip("\n")
            if cnt%2 == 0 and "N" not in line:
                reads.append(line)
            if cnt == limit:
                break
            if not line:
                break
    return reads

def one_fasta(file):
    for seq_record in SeqIO.parse(file,"fasta"):
        return str(seq_record.seq)

#-----------------------------------------------------------

#Organism: Mycoplasma genitalium
#data used:
#whole genome: https://www.ncbi.nlm.nih.gov/data-hub/taxonomy/2097/
#reads: https://trace.ncbi.nlm.nih.gov/Traces/?run=SRR15278551


whole_genome = one_fasta("Mycoplasma genitalium.fasta")
reads = reader("Mycoplasma genitalium reads.fasta", 100)
random_reads = random.choices(reads,k = 30)




#print(suff_arr(string1))


#print(whole_genome.find(reads[0]))
#print(random_reads[0])


#start = time.time()
reconstructed_reads = greedy_scs(random_reads)

#print(time.time() - start)
print(reconstructed_reads)
print(reconstructed_reads in whole_genome)


