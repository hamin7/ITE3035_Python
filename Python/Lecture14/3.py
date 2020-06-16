# fibonacci
# 1, 1, 2, 3, 5, 8, 13

def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

n = int(input('n:'))
print('fibo', n, '=', fibo(n))