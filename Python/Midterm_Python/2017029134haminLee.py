# 1번
# 2017029134
# 이하민

print('점수를 입력해 주세요')
# score를 입력 받아 int 타입으로 수정
score = int(input())

# 올바른 점수가 입력 되었다면 학점을, 아니라면 error를 할당.
if score >= 0 and score < 60:
    grade = '학점 : F'
elif score >= 60 and score < 80:
    grade = '학점 : B'
elif score >= 80 and score < 95:
    grade = '학점 : A'
elif score >= 95 and score <= 100:
    grade = '학점 : A+'
else:
    grade = 'error'

print('your score =', str(score), grade)

# 2번
# 2017029134
# 이하민

print('입력한 숫자만큼의 행으로, 별을 증가하여 출력합니다. 몇 줄을 출력할까요. (1~10 사이)')
num = int(input())

# 올바른 숫자 구간 이라면
if num > 0 and num <= 10:
    cnt = 0
    while True:
        cnt += 1
        if cnt > num:
            break   # 전부 수행했으니 탈출 (종료)
        print('*'*cnt) # cnt 번 출력
# 숫자 구간이 틀렸다면
else:
    print('error')

# 3번
# 2017029134
# 이하민

realPw = 'hy2020'
count = 0

while True:
    print('암호를 입력하세요. q를 입력하면 프로그램이 종료됩니다.')
    yourPw = input()
    count += 1

    if realPw == yourPw:
        print(count, '번 만에 성공하였습니다')
        break   # 성공하였으니 탈출(종료)
    elif yourPw == 'q':
        print('end')
        break   # 에러가 났으니 탈출 (종료)

# 4번
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

# 5번
# 2017029134
# 이하민

# 2017029134
# 이하민

import time

print('몇초 후 알람을 할까요.(1~5초 사이만 설정 가능합니다)')
sec = int(input())

if sec > 0 and sec <= 5:
    time.sleep(sec) # 입력된 초 만큼 정지.
    cnt = 0
    while True:
        cnt += 1
        if cnt > 3:
            break   # 출력 왼료 했으므로 탈출(종료)
        time.sleep(sec) # 입력된 초 만큼 정지.
        print('땡'*cnt) # cnt번 만큼 출력
else:
    print('error')
