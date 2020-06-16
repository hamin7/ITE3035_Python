num=[1,2,3,4,5,6,7,8]
print(type(num))

num.append(6)
num.insert(2,100)

name = ['kim','lee','jung']
a = [num, name]

num.remove(1)
print(num)

del num[0]
print(num)

if 100 in num:
    num.remove(100)

print(num)

for i in num:
    print(i)

test = []
sum = 0
n = int(input('n:'))
for i in range(n):
    val = int(input('num:'))
    test.append(val)

print(test)