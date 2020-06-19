number = int(input('input:'))
count = 0
for i in range(1, number + 1):
    current = i
    temp = count
    while current != 0:
        if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
            count += 1
            print("*")
        current = current
    if temp == count:
        print(i)