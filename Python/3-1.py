print('hello what is your name')
myName = input()
realDay = 5
print('well,', myName, 'guess my birthday from 1 to 30.')
guessDay = input()
guessDay = int(guessDay)
if guessDay != realDay:
    print('Wrong')
if guessDay == realDay:
    print('excellent!')