import random

# 4개의 리스트를 각각 만들고, 각 리스트에는 성격이 비슷한 아이템을 2개 
colors=['pink','orange']
top=['top1','top2']
bottom=['b1','b2']
acce=['a1','a2']

# 1번에서 만든 리스트를 이용해서 오늘의 패션 
a = random.randint(0,1)
print('오늘의 패션 1번 추천 조합입니다')
print(colors[a],'',top[a])
print(colors[a],'',bottom[a])
print(colors[a],'',acce[a])

# 앞에서 작성한 리스트들을 아이템으로 하는 life라는 이름의 리스트를 작성
life=[colors,top,bottom,acce]

# prac4
del colors[1]
print(colors)
top.append('dress')
print(top)
acce[1]='hair band'
print(acce)
print(colors[0]+top[1]+bottom[1]+acce[0])