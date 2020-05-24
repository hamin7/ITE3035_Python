def tillSum(n):
    sum = 0
    for i in range(n+1):    # 0 ~ n
        sum = sum + i
    print('1 ~', n,'까지의 합:', sum)

n = int(input('n:'))
tillSum(n)