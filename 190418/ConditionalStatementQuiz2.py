# This is a guess the number game.

import random

answer = random.randint(1, 20)
while 1:
    print('Take a guess.') # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    if guess < answer:
        result = "Oops! Your guess is too low."
    if guess > answer:
        result = "Oops! Your guess is too high."
    if guess == answer:
        break
    print(result)

if guess == answer:
    result = "Nice! your guess matched the answer"
    print(result)

