def getVal():
    return (float(input('radius:')))

def getArea(n):
    return (3.14*n*n)

a = getVal()
b = getArea(a)
print('Radius:',a,'area:',b)