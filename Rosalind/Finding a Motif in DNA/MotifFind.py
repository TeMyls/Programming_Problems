def motifind(file):
    with open(file,"r") as f:
        data = f.readlines()
        string = data[0].strip()
        pattern = data[1].strip()
        emt_arr = []
        for i in range(len(string) - len(pattern)):
            if string[i:i+len(pattern)] == pattern:
                emt_arr.append(str(i + 1))

        print(" ".join(emt_arr))
        
                
motifind('rosalind_subs.txt')
