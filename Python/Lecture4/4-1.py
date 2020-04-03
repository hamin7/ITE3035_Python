import random

num = random.randint(1,100)
# random.randint(100,40) 작은 수 - 큰 수
# random.randint(1.5,100) 정수만
# random.randint(1) 시작과 끝 있어야
# random.randint(1,2,3) 세개만 있어야
print(num)

print('숫자를 입력하세요')
b = int(input())
if b >= 1:
    newNum = random.randint(1,b)
    print(newNum)

print('두 숫자를 입력하세요', end='')
c = int(input())
d = int(input())

if c < d:
    e = random.randint(c,d)
elif c > d:
    e = random.randint(d,c)
else:
    e = c

print(e)