'''
stinfo # n번 학생의 신상정보 (학과, 학sus, grade) 출력
circle_area(n) # 반지름이 n인 원의 넓이
'''

def circle_area(n):
    print('area', n*n*3.14)

radius = int(input('반지름:'))
circle_area(radius)