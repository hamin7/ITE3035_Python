num=int(input()) 
count=0
for i in range(1,num+1): 
    for j in str(i):
        if j=="0": 
            continue
        elif int(j)%3==0: 
            count+=1
    if count==0: 
        print(i)
    else:
        print("*" * count) 
        count=0