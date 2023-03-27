from Bio import SeqIO


         
def OL_graph(file,k):
    dct = {}
    for seq_record in SeqIO.parse(file,"fasta"):
        string = str(seq_record.seq)
        suffix = string[-k:]
        preffix = string[:k]
        dct.update({seq_record.id:[preffix,suffix]})
    arr = list(dct.keys())
    with open("answe.txt",'w') as f:
        lines = []
        
        for i in dct:
            for j in dct:
                if j != i:
                    if dct[i][0] == dct[j][1]:
                        if [i,j] not in lines and [j,i] not in lines:
                            lines.append([i,j])
                    if dct[i][1] == dct[j][0]:
                        if [i,j] not in lines and [j,i] not in lines:
                            lines.append([i,j])
        
        
      
        
        
        
        for k in lines:
            f.write(f'{k[0]} {k[1]}\n')
            
        
    
    
OL_graph('rosalind_grph.txt', 3)
        

