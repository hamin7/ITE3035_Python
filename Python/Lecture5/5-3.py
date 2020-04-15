import random

print('my name is Alice. your name?')
myName=input()
realDay=random.randint(1,30)
print(myName,'','guess my birthday(1~30)')

trial = 0
while trial <= 5:
    trial=trial+1
    guessDay=int(input('guess:'))
    if guessDay < realDay:
        print('guess a later day')
    if guessDay > realDay:
        print('guess a earlier day')
    if guessDay == realDay:
        print('Correct!')
        break

print('my birth day is', realDay)