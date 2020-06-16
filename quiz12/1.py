def draw_star(n):
    n = n+1     # 지역변수 n
    for i in range(1, n):
        print('*'*i)


n = int(input('n:'))    # 전역변수 n
draw_star(n)
