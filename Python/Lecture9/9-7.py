'''
stinfo # n번 학생의 신상정보 (학과, 학sus, grade) 출력
circle_area(n) # 반지름이 n인 원의 넓이
'''

def stinfo(n):
    if n > 3 or n < 1:
        print('error')
    if n == 1:
        print('''
        1번 학생 : 김연아
        학과 : 소프트웨어
        학년 : 3학년
        특기 : JAVA
        ''')

    if n == 2:
        print('''
        1번 학생 : 이연아
        학과 : 신소재
        학년 : 1학년
        특기 : Python
        ''')

    if n == 3:
        print('''
        1번 학생 : 홍연아
        학과 : 컴공
        학년 : 1학년
        특기 : C++
        ''')

print('몇번 학생의 정보를 알고 싶으신가요?')
n = int(input())
stinfo(n)