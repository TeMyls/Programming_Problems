def hamming_dist(s1,s2):
    return len([i for i in range(len(s1)) if s1[i] != s2[i]])



with open("rosalind_hamm.txt","r") as f:
    data = f.readlines()
    print(hamming_dist(data[0],data[1]))