import random

def opening():
    print('''
    ----------인생역전프로그램----------
    축하합니다. 당신은 인생역전 프로그램에서 최후의 1인이 되어 마지막 선택을 해야합니다.
    당신 앞에는 천사카드와 악마카드가 뒤집어져 있습니다.
    천사카드를 고르면 상금 10억원을 타게 될 것이고
    악마카드를 고르면 모든것을 잃고 빈손으로 돌아가게 됩니다.
    ''')

def drawAngel():
    print('''
    ----------
    | 천사 |
    ----------
    ''')
    print('천사카드. 축하합니다. 10억을 받게 되셨습니다.')
    print('''
    ----------
    1,000,000,000
    ----------
    ''')

def drawEvil():
    print('''
    ----------
    | 악마 |
    ----------
    ''')
    print('안타깝게도 당신은 모든것을 잃고 빈손으로 집으로 돌아가게 되었습니다.')

opening()
chance = random.randint(1,2)
ans = 'yes'
while ans != 'no':
    choice = int(input('어떤 카드를 고르시겠습니까? (1) ir (2):'))
    if choice == chance:
        drawAngel()
        ans = input('시간을 되돌려 카드를 다시 선택하시겠습니까? yes or no:')
    else:
        drawEvil()
        ans = input('시간을 되돌려 카드를 다시 선택하시곘습니까? yes or no:')