def draw_star(n):
    for i in range(n):
        j = 0
        while j <= i:
            if j <= i:
                print('*', end='')
            j = j + 1
        print()


n = int(input('n:'))    # 전역변수 n
draw_star(n)
