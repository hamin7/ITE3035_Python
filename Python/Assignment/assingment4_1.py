print('정수를 입력해 주세요: ', end='')
n=int(input())
count = 1
sum=0

while count <= n:
    if count%2 == 0:
        sum = sum + count
    count = count + 1

print('1~'+str(n)+'까지 2의 배수의 합: '+str(sum))
