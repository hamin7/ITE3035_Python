'''
의문점
1. 도망치다 잡히는지, 잘 도망치는지는 random으로 하는가 아니면 선택하는가?
2. 도망에 실패하면 무조건 죽는 것인가? 아니면 싸우는 것인가?
3. 싸움에서 지면 게임 끝? 프로그램 종료?
4. 곰을 마주칠 확률은 내 마음대로?
5. 1초 멈추는 것을 다른곳에서도 해도 되는지? ㅇㅇㅇ
6. 싸울지 선택하는 것은 랜덤 함수로 아니면 사용자가 입력하도록?
'''

import random
import time
import sys

count = 0   # 나무를 찍은 횟수.

# count가 9가 될 때 까지 (0 ~ 9, 10번) 나무를 찍는 반복문.
while count < 10:
    count = count + 1
    print('나무꾼이 나무를', count,'번 찍었습니다.🪓')
    isBearAppear = random.randint(0,10)  # 이번 회차에 곰과 만날 지 여부, 3이하라면 곰을 마주침.
    
    # 곰과 만났다면.
    if isBearAppear <= 3:
        print('곰과 마주쳤습니다🐻 맞서 싸우시겠습니까? (싸우고 싶다면 1, 도망가고 싶다면 2을 입력.) ', end='' )
        bearStamina = 100   # 곰의 체력, 100에서 시작.
        wantFight = int(input())     # 곰과 싸울지 여부, 0이면 도망, 1이면 싸움.

        # 싸우길 원한다면.
        if wantFight == 1:
            print('곰과 싸웁시다.💪')
            time.sleep(1)
            
            # 곰과 싸우기.
            fightCount = 0  # 몇 번 공격했는지.
            # 6회까지 공격 가능.
            while True:
                attack = random.randint(1,30)   # 1회 공격력.
                fightCount = fightCount + 1     # 공격 횟수 1개 증가.
                bearStamina = bearStamina - attack
                if bearStamina <= 0:
                    bearStamina = 0 # 곰의 체력이 음수가 되면 체력을 0으로 표시한다.
                    print(fightCount,'회 공격은 곰에게 ',attack,'의 타격을 입혀 곰의 체력이 ',bearStamina,'이 되어 싸움에서 승리하셨습니다.🗽')
                    break   # 싸움 루프에서 탈출.
                elif bearStamina > 0 and fightCount < 6:
                    print(fightCount,'회 공격은 곰에게 ',attack,'의 타격을 입혀 곰의 체력이 ',bearStamina,'가 되었습니다.👏')
                    time.sleep(1)
                # 6번을 공격하였는데 곰의 체력이 0보다 크다면 => 싸움에서 짐.
                elif bearStamina > 0 and fightCount == 6:
                    print('싸움에서 패배하셨습니다. 나무 찍기에 실패하였습니다. 프로그램을 종료합니다.👻')
                    sys.exit()
        
        # 도망가길 원한다면.
        elif wantFight == 2:
            print('도망갑니다!')
            successfulEscape = random.randint(0,1)  # 도망 성공 여부, 0이면 실패 1이면 성공.
            if successfulEscape == 0:
                print('성공적으로 도망쳤습니다👍🏼')
            elif successfulEscape == 1:
                print('도망에 실패했습니다❗️')
                print('나무 찍기에 실패하였습니다. 프로그램을 종료합니다.👻')
                sys.exit()
            else:
                print('에러입니다.🤯')
        else:
            print('에러입니다.🤯')
    # 곰을 만나지 않았다면
    elif isBearAppear > 3:
        print('곰이 없군요~😁')
    # 에러 (곰을 만났는지 여부가 0도 1도 아닐 때)
    else:
        print('에러입니다.🤯')
    
    time.sleep(1)   # 나무를 찍은 후 1초 멈춤.

print('나무찍기 10번을 성공하였습니다! 🍾')