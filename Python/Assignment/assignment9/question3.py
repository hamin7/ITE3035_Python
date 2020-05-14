def draw(n):
    cnt = 0
    while cnt < n:
        cnt += 1
        print('*' * cnt)

print('몇줄을 출력할까요 (1~10)')

while True:
    
    print('n: ', end="")
    n = int(input())
    if n > 0 and n <= 10:
        draw(n)
        break
    else:
        print('error')