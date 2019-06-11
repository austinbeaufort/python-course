# i = 1

# while i <= 5:
#     print('*' * i)
#     i += 1

# print('done')








EXERCISE: GUESS THE NUMBER GAME

secret_number = 9
guess_count = 0
guess_limit = 3

print('Guess my Secret Number!')
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('Yay you Won!')
        break
else:
    print('Sorry, you Lose!')    

    
