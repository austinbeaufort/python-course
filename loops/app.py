# EXERCISE: GUESS THE NUMBER GAME

SECRET_NUMBER = 9
GUESS_COUNT = 0
GUESS_LIMIT = 3

print('Guess my Secret Number!')
while GUESS_COUNT < GUESS_LIMIT:
    guess = int(input('Guess: '))
    GUESS_COUNT += 1
    if guess == SECRET_NUMBER:
        print('Yay you Won!')
        break
else:
    print('Sorry, you Lose!')
