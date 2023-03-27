#https://github.com/gittenberg/rosalind/blob/master/Mortal%20Fibonacci%20Rabbits.py

def MortalFibonacci(n, m):
    living = [1, 1]
    for i in range(2, n):
        # first reproduction
        tmp = living[i - 1] + living[i - 2]
        # then death
        if i == m:
            tmp = tmp - 1
        if i > m:
            tmp = tmp - living[i - m - 1]
        living.append(tmp)
    return living[-1]


with open("rosalind_fibd.txt",'r') as f:
   data = f.read().split(' ')
   months = int(data[0])
   offspring = int(data[1])
   print(MortalFibonacci(months,offspring))