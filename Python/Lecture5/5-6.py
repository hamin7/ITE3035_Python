# 윤년 판별
print('enter year:')
year=int(input())

if year%4==0 and year%100!=0 or year%400==0:
    print('leaf year')
else:
    print('common year')