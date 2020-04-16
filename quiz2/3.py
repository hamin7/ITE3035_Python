print('앵무새 프로그램입니다. 아무말을 다섯 번 해주세요!')

trial = 0
while trial <= 5:
    trial=trial+1
    print('사용자: ', end='')
    comment = input()
    print('앵무새:', comment)
    print()