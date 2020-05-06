print('''도서관에서 열심히 공부하던 당신은 바람을 쐬기 위해 잠깐 나왔습니다. 마침 자판기가 보이네요''')
print('''
-------------------------------------
|                                   |
|      밀크티/에너지드링크/콜라     |
|                                   |
-------------------------------------
''')
money = int(input('자판기에 얼마를 넣을지 입력하세요:'))
print('(1) 밀크티 700 (2) 에너지 드링크 800 (3) 콜라 600 (4) 잔돈받기')
print('제품 금액보다 넣은 돈이 적으면 잔돈이 자동 반환 됩니다')

choice = int(input('선택:'))
if choice == 1:
    if money >= 700:
        print('덜커덩 밀크티')
        money = money - 700
        print('잔돈 지급:','딸그랑 ~ '*int(money/100))
    else:
        print('잔돈부족')
        print('잔돈 지급:','딸그랑 ~ '*int(money/100))
elif choice == 2:
    if money >= 800:
        print('덜커덩 에너지 드링크')
        money = money - 800
        print('잔돈 지급:','딸그랑 ~ '*int(money/100))
    else:
        print('잔돈부족')
        print('잔돈 지급:','딸그랑 ~ '*int(money/100))
elif choice == 3:
    if money >= 600:
        print('덜커덩 콜라')
        money = money - 600
        print('잔돈 지급:','딸그랑 ~ '*int(money/100))
    else:
        print('잔돈부족')
        print('잔돈 지급:','딸그랑 ~ '*int(money/100))
else:
    print('잘못 입력')
    print('잔돈 지급:','딸그랑 ~ '*int(money/100))