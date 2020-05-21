import random

print('로또번호 생성 프로그램')
print('===============')
count = 1

while count <= 6:
    lotto = random.randint(1,45)
    print(count, '번쨰 번호는 ', lotto, '입니다.')
    count = count+1
