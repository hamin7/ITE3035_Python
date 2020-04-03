import random

print('a')
a = int(input())    # int(input('a:'))
print('b')
b = int(input())    # int(input('b:'))
if a > b:
    ranum = random.randint(a,b)
    print(a,'부터',b,'까지에서 무작위로 선택한 숫자는', ranum,'입니다.')
elif a < b:
    ranum = random.randint(b,a)
    print(b,'부터',a,'까지에서 무작위로 선택된 숫자는',ranum,'입니다.')
else:
    print('두 수가 같습니다')