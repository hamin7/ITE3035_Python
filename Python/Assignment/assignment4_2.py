print('단을 입력하세요(1~9): ', end='')
dan = int(input())
count=1
print('______________________________')
while count <= 9:
    print(dan,'*',count,'=',dan*count)
    count=count+1

print('______________________________')