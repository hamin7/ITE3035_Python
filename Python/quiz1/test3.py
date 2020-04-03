print('정수 숫자 두 개를 입력해 주세요')
print('num1:', end='')
num1 = int(input())
print('num2:', end='')
num2 = int(input())

if num1 > num2:
    print('Max: '+ str(num1)+' Min: '+ str(num2) + ' diff, two number= '+str(num1-num2))
elif num1 < num2:
    print('Max: '+ str(num2)+' Min: '+ str(num1) + ' diff, two number= '+str(num2-num1))
elif num1 == num2:
    print('Max: '+ str(num1)+' Min: '+ str(num2) + ' diff, two number=0, two number is same ')