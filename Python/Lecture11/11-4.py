realPW='good'
def getPw():
    for i in range(3):  # 0 ~ 2까지 총 3회의 기회를 준다.
        print('enter PW:')
        pw = input()
        if pw == realPW:
            print(i+1,'회 만에 맞추었다')
            break

getPw()