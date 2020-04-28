# 2017029134
# 이하민

count = 0
sum = 0
print('0 ~ 100 까지의 숫자를 입력하세요')

while True:
    a = input()
    if a == 'q':
        break   # q가 입력되면 탈출
    else:
        a = int(a)  # str을 int로 변환
        if count == 0:
            max = a # 첫 값으로 max 할당
            min = a # 첫 값으로 min 할당
        else:
            if a > max:
                max = a
            elif a < min:
                min = a
        sum += a
        count += 1

avg = sum / count
print('sum:', sum, 'average:', avg)
print('Max:', max, 'Min:', min)
