import random

n = int(input('투표자 수:'))
m = int(input('후보자 수:'))
f = []

for i in range(m):
    f.append(0)     # 초기값이 있어야 더해질 수 있음

for i in range(n):
    tp = random.randint(1,3)
    f[tp-1] = f[tp-1] + 1

for i in range(m):
    print(i+1,'번쨰 후보의 투표 빈도:', f[i])
