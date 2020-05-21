import random

print('숫자를 입력하세요.')

while True:
    num = int(input())
    if num <= 0:
        print('다시 입력해주세요.')
    elif num > 0:
              randNum = random.randint(1,num)
              print('1부터',num,'까지에서 무작위로 선택된 값은',randNum,'입니다')
              break
