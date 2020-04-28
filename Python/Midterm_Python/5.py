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