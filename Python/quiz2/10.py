import sys

print('숫자를 입력하세요.')
count = 1
sum = 0
max = 0
min = 100

while True:
    num = input()
    if num == '입력 끝':
        break
    elif int(num) < 0 or int(num) > 100:
        print('처리 할 수 없는 숫자 입니다')
        sys.exit()
    elif int(num) > 0 and int(num) < 100:
        num = int(num)
        sum = sum + num
        if num > max:
            max = num
        if num < min:
            min = num
        count = count + 1
    else:
        sys.exit()
     
mean = sum/(count-1)

print('입력받은 숫자들의 합은', sum)
print('입력받은 숫자들의 평균은', mean)
print('가장 큰 숫자는',max)
print('가장 작은 숫자는',min)
        
