def calc(divisor):
    num1 = input('나누어지는 숫자:')
    result = int(num1) / int(divisor)
    return result

num = input('나누는 숫자:')
qu = calc(num)
print('몫은',qu,'입니다.')