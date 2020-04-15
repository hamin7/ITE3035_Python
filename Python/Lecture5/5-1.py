#2 1~9까지 숫자 중 dan 입력 후 구구단 출력
dan = int(input('dan: '))
i = 1
print(dan,'단')
print('-------------------------')
while i <= 9:
    print(dan,'*',i,'=',dan*i)
    i=i+1