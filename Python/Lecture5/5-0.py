'''
복습
random.randint error case
    - (a, b) a가 더 큰 경우
    - (10.5, 20) 실수가 포함된 경우
    - (1)인수가 모자랄 경우
    - (1, 2, 3) 인수가 과할 경우.

While
- 반복문 - 조건 비교 결과가 True인 동안 블록 소스코드 반복

while 조건 비교:
    실행 문장1
    실행 문장2
    실행 문장3
'''

#1 1 ~ n까지의 2의 배수의 합

sum=0
n=int(input('n: '))
i = 0
while i <= n:
    if i%2 == 0:
        sum = sum + i
    i = i + 1

print('0~',n,'까지의 2의 배수의 합:',sum)