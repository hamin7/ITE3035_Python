'''
- 다음 세 개의 사용자 정의함수 사용 
def val(): # 정수값 하나 리턴
def draw1(n): # ‘*’을 n의 횟수만큼 한줄에 그리기  (ex: n이 3이면, ***)
def  draw2(n): # n-1 라인의 역삼각형 그리기 
모든 사용자 정의 함수에 지역변수 n을 사용하고, 전역변수 역시, n으로 호출합니다. 이외 필요한 변수는 자유롭게 사용합니다. 
반복문 사용 시, for문을 사용합니다. for는 range를 사용하고, start는 1로 설정합니다. 
각 사용자 정의함수의 코드는 각 4라인 이내로 작성해 주세요. 

<결과>
n: 4
***
**
*
'''
def val(): # Return the integer 'n' value
   n = int(input('n:'))
   return n

def draw1(n): # Draw '*' as much as 'n' on one line
    for i in range(1,n+1):
        print('*',end='')
    print()

def  draw2(n): # Draw a right triangle of 'n' line
    for i in range(1,n+1):
        draw1(n-i)

n=val()
print(n)
draw2(n) 