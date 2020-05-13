# 험수명 : add, sub, mul, div

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

print('사칙연산 해봅시다. 1)add, 2)sub, 3)mul, 4)div, 5)quit')
choice = int(input())
if choice == 1:
    print(add(1,2))
elif choice == 2:
    print(sub(1,2))
elif choice == 3:
    print(mul(1,2))
elif choice == 4:
    print(div(1,2))
elif choice == 5:
    print('end')
else:
    print('wrong num')

# 반복문을 이용하고, quit(5)나, 1~5가 아닌 수를 선택하면 반복 탈출
# a,b도 반복 횟수만큼 입력받을 수 있도록 함.