'''
#10
sum=0
count=1
print('0~ 100 까지의 숫자를 입력하세요')
max=-999 #-1
min=999 #101
while True:
    a=input()
    if a=='입력끝':
        break
    a=int(a)
    if a>100 or a<0:
        print('error')
        break
    if a>max:
        max=a
    if a<min:
        min=a
    sum=sum+a
    count=count+1

print('sum:',sum,' ' ,'average: ',sum/(count-1))
print('Max:',max,' ','Min:',min)
        

'''
#9
import random
num=int(input('num: '))
while num<1:
    print('다시 ! ')
    num=int(input('num: '))

num2=random.randint(1,num)
print('1~',num,'까지의 무작위 선택값은',num2,'입니다')
#8
pw='python'
while True:
    yourPw=input('암호를 입력하세요:')
    if yourPw==pw:
        print('S')
        break
    print('암호가 바르지 않습니다\n\n\n')


#7
i=1
money=100
print('티끌모아 태산')
print()
while i<=7:
    print('땡그랑, '*i,'동전 ',money,'을 모았습니다')
    i=i+1 #i+=1
    money=money+100 #money+=100

#6
import random
print('로또 번호 생성 프로그램')
print('==================')

i=1
while i<=5:
    a=random.randint(1,45)
    print(i,'번째 번호 :', a)
    i=i+1


#5
sum=0
i=1 # 증가할 숫자
while i<=100:
    sum=sum+i
    i=i+1
print('sum of 1 ~ 100 :',sum)

#4
i=1
while i<=5:
    print('*'*i)
    i=i+1
#3
i=1
while i<=5:
    a=input('사용자:')
    print('앵무새:'+a)
    i=i+1

#2
a=input('사용자:')
print('앵무새:' +a)

#1
print('score')
score=int(input())
while True:
    if score>100 or score<0:
        print('error')
        break
    if score>=90:
        print('pass')
        break
    else:
        print('fail')
        break'''
