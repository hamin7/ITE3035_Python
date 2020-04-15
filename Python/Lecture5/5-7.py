import random
com = random.randint(1,6)
print('주사위 번호 맞추기')

yours=0
count=0
while True:
    yours=int(input('your number: '))
    if yours == com:
        print('Correct!')
        print('your trial:', count)
        break
    print('다시!')
    count=count+1