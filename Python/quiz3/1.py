import random
chance=random.randint(1,10) # 1~10사이의 랜덤수 대입 
count=0 

while True: #무한반복
    choice=input('행운의 번호를 고르세요(1~10):')
    count=count+1
    if int(choice)==chance:
        print(count,'번만에 찾아온 행운 \\\\♡----->Lucky//') # ‘* 번만에 찾아온 행운  \\♡----->Lucky// ’ 과 같은 글자 출력 후 반복중단 
        break 
    else:
        if chance < int(choice): # 아래 문자열이 나올 수 있는 조건 설정 
            print('당신이 선택한 수보다 작습니다')
            ans=input('번호를 다시 고르시겠어요?(y/n) : ')
            if ans == 'n': break #바로 윗줄에서 n를 고르면 반복중단 
            if ans != 'y': break
        else:
            print('당신이 선택한 수보다 큽니다')
            ans=input('번호를 다시 고르시겠어요?(y/n):')
            if ans == 'n': break # 바로 윗줄에서 n를 고르면 반복중단 및
            if ans != 'y': break