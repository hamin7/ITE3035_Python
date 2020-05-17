import random

def getCardNum():
    while True:
        result = int(input('user Num:'))
        if result == 1 or result == 2:
            break
        return result

# p166
def compareCard(result):
    choice = random.randint(1,2)
    if choice == result:
        print('천사카드')
    else:
        print('악마카드')

a = getCardNum()
compareCard(a)