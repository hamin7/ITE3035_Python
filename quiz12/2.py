realPW = 'good'
def getPw():
    for i in range (3):
        print('enter PW:')
        enterPW = input()
        if realPW == enterPW:
            print(i+1, '회만에 맞추었습니다. 축하드립니다')
            break
        else:
            if i == 2:
                print('암호맞추기 프로그램을 종료합니다. ㅜㅜ')
                break
            elif i == 0 or i == 1:
                print('힌트: g로 시작합니다')

print('암호를 입력하세요. 기회는 총 3번')
getPw()
