# 2017029134
# 이하민

print('점수를 입력해 주세요')
# score를 입력 받아 int 타입으로 수정
score = int(input())

# 올바른 점수가 입력 되었다면 학점을, 아니라면 error를 할당.
if score >= 0 and score < 60:
    grade = '학점 : F'
elif score >= 60 and score < 80:
    grade = '학점 : B'
elif score >= 80 and score < 95:
    grade = '학점 : A'
elif score >= 95 and score <= 100:
    grade = '학점 : A+'
else:
    grade = 'error'

print('your score =', str(score), grade)