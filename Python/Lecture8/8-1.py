money = 1000

p1 = 500
p2 = 300
p3 = 800

print('음료를 선택하세요')

choice = int(input())

if choice == 1:
    rest = 1000-500
elif choice == 2:
    rest = 1000-300
elif choice == 3:
    rest = 1000-800
else:
    rest = 1000

print('잔돈 : ',rest)