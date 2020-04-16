print('점수를 입력하세요. (1~100점)')
score = int(input())
if score < 0 or score > 100:
    print('잘못된 입력입니다. 종료합니다.')
if score > 0 and score < 100:
    if score >= 90:
        print('합격입니다.')
    if score < 90:
        print('불합격입니다.')
        

