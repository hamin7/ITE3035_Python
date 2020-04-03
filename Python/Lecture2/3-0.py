print() # 한 줄 띄기
print('string'+'string')
print(5+10)
print('string',5,'string')
print('string'*5)

input()
# 키보드로부터 숫자, 문자 등을 입력 받아 변수에 저장
# 모든 입력값은 string으로 변환

age = input('age:')
type(age)   # 해당 변수의 타입을 알아보기

int(input('age:'))
# 문자열을 정수형으로 변환하려면 int()

end=''  # 줄이 바뀌지 않고 공백만 추가.
print('hi',end='')
print('good') 