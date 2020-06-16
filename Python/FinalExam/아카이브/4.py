def getVal():
    val = int(input('n:'))
    return val

def result(n):
    print('n의 factorial=', fac(n))
    print('n의 fibonacci value=', fibo(n))

def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
def fac(n):
    factorial=1
    for i in range(1,n+1):
        factorial=factorial*i
        
    return factorial

n=getVal()
result(n)