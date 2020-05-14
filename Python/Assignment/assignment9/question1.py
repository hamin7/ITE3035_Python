def test(score):
    if score >= 70:
        print('합격입니다')
    else:
        print('불합격입니다')

print('점수를 입력해 주세요 (0 ~ 100)')
while True:
    print('score : ', end='')
    score = int(input())
    if score >= 0 and score <= 100:
        test(score)
        break
    else:
        print('error')
