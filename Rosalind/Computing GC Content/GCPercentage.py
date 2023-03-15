from Bio import SeqIO
def CG_Counter(file):
    highest_percentage = 0
    highest_id = ""
    for seq_record in SeqIO.parse(file,"fasta"):
        Gs = 0
        Cs = 0
        seq_len = len(seq_record)
        for i in str(seq_record.seq):
            if i == "G":
                Gs += 1
            elif i == "C":
                Cs += 1
        if ((Gs + Cs)/len(seq_record))*100 > highest_percentage:
            highest_percentage = ((Gs + Cs)/len(seq_record))*100 
            highest_id = seq_record.id
            
    print(highest_id,round(highest_percentage,6),sep = "\n")
            
            
CG_Counter("rosalind_gc.txt")                
        
    