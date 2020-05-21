password='Python'
while True:
    print('암호를 입력하세요.')
    yourpw=input()
    if password == yourpw:
        print('로그인 성공')
        break
    else:
        print('암호가 올바르지 않습니다.')
