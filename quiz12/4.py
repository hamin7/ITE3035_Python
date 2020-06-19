n = int(input("Please enter the number:"))
for i in range (1,n+1): #print(i)
    if(i >= 1 and i <30):
        if(i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
            print("*")
            continue 
        else:
            print(i)
    elif(i >= 30 and i <= 40):
        if(i % 10 == 3 or i % 10 == 6 or i % 10 == 9): 
            print("**")
            continue
        elif(i != 40): 
            print("*")
        else:
            print(i)
    else:
        break