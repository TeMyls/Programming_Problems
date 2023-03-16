def FirstLaw(k,m,n):
    AA, Aa, aa = k, m, n
    total = k + m + n
    numerator = AA * (AA - 1)  + (AA * Aa + Aa * AA) + (AA * aa + aa * AA) + (.75 * Aa * (Aa - 1))+(.5 * Aa * aa + .5 * aa * Aa)
    demoninator = total * ( total - 1)
    return numerator/demoninator


with open("rosalind_iprb.txt","r") as f:
    data = list(map(int,f.read().split(" ")))
    print(FirstLaw(data[0],data[1],data[2]))