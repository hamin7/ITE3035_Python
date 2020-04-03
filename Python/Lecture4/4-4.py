import random

print('a')
a = int(input())    # int(input('a:'))
print('b')
b = int(input())    # int(input('b:'))
rannum = random.randint(a,b)
print(a,'부터',b,'까지에서 무작위로 선택된 숫자는',rannum,'입니다.')