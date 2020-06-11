ex1 = []
sum = 0
n = int(input('n:'))
for i in range(1,n+1):
    val = int(input('num:'))
    ex1.append(val)


for i in ex1:
    sum = sum + i

print('sum=', sum, 'avg=', sum/n, 'min=', min(ex1), 'max=', max(ex1))
