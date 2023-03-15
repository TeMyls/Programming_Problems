def reverse_complement(string):
    complements = {'A':'T','T':'A','G':'C','C':'G'}
    return ''.join([complements[letter] for letter in string[::-1] if letter != "\n"])


with open('rosalind_revc.txt','r') as f:
    DNA = f.read()
    print(reverse_complement(DNA))

print('*'*4)