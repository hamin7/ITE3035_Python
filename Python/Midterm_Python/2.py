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
