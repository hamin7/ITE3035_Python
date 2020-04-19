while True:
    print('choose dan')
    dan = int(input('dan:'))
    if dan < 1 or dan > 9:
        print('다시')
    if dan > 0 and dan < 10:
        break

count = 1
while True:
    print(dan, '*', count, '=', dan*count)
    count=count+1
    if count > 9:
        break