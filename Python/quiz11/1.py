import random
def test(a):
    ans = 3.14 * a * a
    return ans
ans = 3.14
i = random.randint(1,10)
val = test(i)
print('result : radius: ',i, ' area: ',val)