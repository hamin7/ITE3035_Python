import random

realPw = random.randint(10,99)
print('enter password(10~99)')
authorized='false';

while authorized=='false':
    print('pw: ',end='')
    pw=int(input())
    if realPw==pw:
        print('Correct')
        authorized='true'
    else:
        print('fail. again!')
