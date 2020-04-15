# 이진검색(Binary Seach)

print('I am thinking of a number of from 10 to 50, guess it.')
start=10
end=50
answer=37
guess=input()
if answer > int(guess):
    print('smaller than the answer')
if answer < int(guess):
    print('bigger than the answer')
if answer == int(guess):
    print('correct')