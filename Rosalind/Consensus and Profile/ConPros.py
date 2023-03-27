from Bio import SeqIO

def consensus(file):
    index_matrix = {}
    for seq_record in SeqIO.parse(file,"fasta"):
        for i in range(len(seq_record.seq)):
            index_matrix.update({i:""})
        break
            
    for seq_record in SeqIO.parse(file,"fasta"):
        for i in range(len(seq_record.seq)):
            index_matrix[i] = index_matrix[i] + seq_record.seq[i]
            
    consensus_string = ""
    for i in index_matrix:
        As = 0
        Ts = 0
        Gs = 0
        Cs = 0
        for j in index_matrix[i]:
            if j == "A":
                As += 1
            elif j == "T":
                Ts += 1
            elif j == "G":
                Gs += 1
            elif j == "C":
                Cs += 1
        if As >= Ts and As >= Gs and As >= Cs:
            consensus_string += "A"
        elif Ts >= As and Ts >= Gs and Ts >= Cs:
            consensus_string += "T"
        elif Gs >= As and Gs > Ts and Gs >= Cs:
            consensus_string += "G"
        elif Cs >= Gs and Cs >= As and Cs >= Ts:
            consensus_string += "C"
    print(consensus_string)
        
consensus("mid.txt")
        
        
            

        