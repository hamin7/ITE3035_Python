def calcul_start(n):
    count = 0
    hap = 0

    while count < n:    
        print('score ', count, ' : ', end='')
        score = input()
        if score == 'q':
            print('end')
            break
        else:
            score = int(score)
            hap += score
        count += 1
    
    avg = hap/count
    print('sum : ', hap, ' avg : ', avg)

while True:
    print('입력할 점수의 갯수 (1-10) : ', end='')
    n = int(input())
    if n <= 10 and n >= 0:
        calcul_start(n)
        break
    else:
        print('갯수를 다시 입력해주세요')
