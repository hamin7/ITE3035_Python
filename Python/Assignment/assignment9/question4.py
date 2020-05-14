import random

def lucky(n):
    cnt = 0

    while cnt < n:
        cnt += 1
        num = random.randint(1,100)
        print(cnt, '번째 번호는 ', num, '입니다')

while True:
    print('n(1~5): ', end='')
    n = int(input())

    if n > 0 and n <= 5:
        lucky(n)
        break
    else:
        print('error')
    