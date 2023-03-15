def nucleotide_counter(string):
    As, Cs, Gs, Ts = 0, 0, 0, 0
    for letter in string:
        if letter == "A":
            As += 1
        elif letter == "C":
            Cs += 1 
        elif letter == "G":
            Gs += 1
        elif letter == "T":
            Ts += 1
    return As,Cs,Gs,Ts

with open("rosalind_dna.txt","r") as f:
    DNA = f.read()
    print(nucleotide_counter(DNA))
    
