# 구구단
'''
print('enter dan for gugudan(2~9)')
dan=input('dan:')
# dab = int(input('dan: ')) # 숫자
count=1

while True:
    print(''+dan+'*'+str(count)+'='+str(int(dan)*count))
    # print(dan,'*',count,'=',dan*count)
    count = count+1
    if count > 9:
        break
'''

while True:
    print('enter dan for gugudan(2~9)')
    dan=int(input('dan: '))
    if dan < 1 or dan > 9:
        print('다시')
    if dan > 0 and dan < 10:
        break

print(dan,'단')
count=1

while True:
    # print(''+dan+'*'+str(count)+'='+str(int(dan)*count))
    print(dan,'*',count,'=',dan*count)
    count = count+1
    if count > 9:
        break