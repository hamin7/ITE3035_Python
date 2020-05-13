import random
import time

chance = random.randint(1,2)
print('''
----------인생역전프로그램----------
축하합니다. 당신은 인생역전 프로그램에서 최후의 1인이 되어 마지막 선택을 해야합니다.
당신 앞에는 천사카드와 악마카드가 뒤집어져 있습니다.
천사카드를 고르면 상금 10억원을 타게 될 것이고
악마카드를 고르면 모든것을 잃고 빈손으로 돌아가게 됩니다.
''')
ans = 'yes'
while ans != 'no':
    choice = int(input('어떤 카드를 고르실까요? 1,2'))
    if choice == chance:
        time.sleep(2)
        print('''
        ----------
        | 천사 |
        ----------
        ''')
        print('천사카드. 축하합니다. 100억을 받게 되셨습니다.')
        ans = input('다시 선택하시겠습니까? yes or no')
    else:
        time.sleep(2)
        print('''
        ----------
        | 악마 |
        ----------
        ''')
        print('악마카드. 아쉽다...')
        ans = input('다시 선택하시겠습니까? yes or no')