def val():
    a = int(input('n:'))
    return a

def result(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end='')
        print()

a = val()
result(a)