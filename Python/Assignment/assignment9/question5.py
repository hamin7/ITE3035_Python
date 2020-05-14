def draw2(n):
    cnt = 0
    while cnt < n:
        cnt += 1
        print('\'*\' ',cnt, ' 회 출력','*' * cnt, ' \    \'♡\' ', 2*cnt, ' 회 출력 : ', '♡'*2*cnt)

while True: 
    print('n(1~5): ', end="")
    n = int(input())
    if n > 0 and n <= 5:
        draw2(n)
        break
    else:
        print('error')