import random

print('hello my name is gerrit')
print('what\'s your name?')
myName = input()
realDay = random.randint(1,30)
print('well, ' + myName + ', guess my birthday from 1 to 30')
guessDay = 0

while realDay!=guessDay:
    guessDay = input()
    guessDay = int(guessDay)
    if guessDay < realDay:
        print('later')
    elif guessDay > realDay:
        print('earlier')
    else:
        print('good')