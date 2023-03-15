from Bio.Seq import Seq

with open('rosalind_rna.txt','r') as f:
    coding_strand = Seq(f.read()) 
    RNA = coding_strand.transcribe()
    print(RNA)