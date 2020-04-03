print('연산을 수행할 두 수와, 원하는 연산(1.add, 2.sub, 3.mul, 4.div) 번호를 입력하세요.')
print('num1:', end='')
num1 = int(input())
print('num2:', end='')
num2 = int(input())
print('op:', end='')
op = input()

if op == '1':
    print('연산결과 '+ str(num1) + '+' + str(num2) +'=' + str(num1+num2))
elif op == '2':
    print('연산결과 '+ str(num1) + '-' + str(num2) +'=' + str(num1-num2))
elif op == '3':
    print('연산결과 '+ str(num1) + '*' + str(num2) +'=' + str(num1*num2))
elif op == '4':
    print('연산결과 '+ str(num1) + '/' + str(num2) +'=' + str(num1/num2))
