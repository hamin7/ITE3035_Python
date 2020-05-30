def getVal():
    val = int(input('n:'))
    return val

def fac(n):
    factori = 1
    for i in range(1,n+1):
        factori = factori*i
    return factori

n = getVal()
print(n,'\'s factorial =',fac(n))