start=int(input('start year: '))
end=int(input('end year: '))
print(str(start)+'~'+str(end)+'까지 윤년 목록')
for i in range(start,end):          #
    if ((i/4==0 and i/100 ==0) or (i/400==0)):        #
        print(i, '=  leaf year')