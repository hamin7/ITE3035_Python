import random

def test(a): # error
    ans = 3.14*a*a
    return ans

ans = 3.14
i=random.randint(1,10)  #error
val=test(i) #error
print('radius=',i,'area:', val)

# 지역변수(함수가 끝나면), 전역변수(프로그램이 끝나면)