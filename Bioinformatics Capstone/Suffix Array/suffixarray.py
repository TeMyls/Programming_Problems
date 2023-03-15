import time

string1 = "gctaagttcatgcatc"
arr = ["catg", "ctaagt", "gcta","atgcatc" ,"ttca"]

string2 = "acccgattatatt"
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


def suff_arr(word):
	dct = {word[i:]:i for i in range(len(word))}
	return dict(sorted(dct.items()))
	
	
def merg(string_1,string_2):
	index_dct = suff_arr(string_1)
	for i in range(len(string_2),0,-1):
		k = index_dct.get(string_2[:i])
		if k is not None:
			#print(index_dct[string_1[i:]])
			#print(string_2[:i])
			return string_1[:k] + string_2,len(string_1[k:])
	  	
	return string_1 + string_2,0
	 
def merg(string_1,string_2):
	index_dct = suff_arr(string_1)
	for i in range(len(string_2),0,-1):
		k = index_dct.get(string_2[:i])
		if k is not None:
			#print(index_dct[string_1[i:]])
			#print(string_2[:i])
			return string_1[:k] + string_2,len(string_1[k:])
	  	
	return string_1 + string_2,0
	 
def scs(arr):
	max_overlap, index_1,index_2,true_string = 0 ,0 ,0 ,""
    #print(len(arr))
	#print(arr)
	if len(arr) == 1:
		return arr[0]
    
	for j in range(1,len(arr)):
		string_overlap = merg(arr[0],arr[j])
		overlap_string = merg(arr[j],arr[0])
		if string_overlap[1] > overlap_string[1]:
			if string_overlap[1] >= max_overlap:
				max_overlap = string_overlap[1]
				true_string = string_overlap[0]
				index_1 = 0
				index_2 = j
		elif string_overlap[1] < overlap_string[1]:
			if overlap_string[1] >= max_overlap:
				max_overlap = overlap_string[1]
				true_string = overlap_string[0]
				index_1 = 0
				index_2 = j
		
		
			
    
    #print(max_overlap)
    #removal from array has to be like this so the indexing doesn't mess up       
	arr.pop(index_2)
	arr.pop(index_1)
    
    
    
	arr.append(true_string)
	return scs(arr)
print(suff_arr("AGAGTCATCCAGCTGGAGCCCTGAGTGGCTGAGCTCAGGC"))
#print(g)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~







print(scs(arr))

