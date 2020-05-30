def val():
    a= int(input('n:'))
    return a

def result(n):
    for i in range(1, n):
        for j in range(i+1):
            print(j+1, end=' ')
        print()
        
a=val()
result(a)