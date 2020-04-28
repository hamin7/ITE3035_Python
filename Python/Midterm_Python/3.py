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