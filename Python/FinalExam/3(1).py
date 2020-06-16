finalEx1=[]
sum=0       #
n=int(input('n : '))
for i in range(1,n+1):      #
    val=float(input('num: '))
    finalEx1.append(val)        # 

for i in finalEx1:
    sum=sum+1 
sum=sum+1 #반올림 
print(' 반올림된 합(sum): ', int(sum), '\n', ' 반올림된 sum에 대한 평균 (avg.. 구해진 몫에 대하여 반올림하여 출력) =', int(sum/n))