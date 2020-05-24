def getVal():
    val = int(input('n:'))
    return val

def fac(n):
    factorial = 1
    for i in range(1,n+1):  # 1 ~ n+1-1
        factorial = factorial*i # 1*1*2*3*4*5
    return factorial

a = getVal()
b = fac(a)
print('1~',a,'Factorial:',b)