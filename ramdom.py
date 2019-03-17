import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')
for guessesTaken in range(1, 7):
    print('take a guess: ')
    guess = int(input())

if guess < secretNumber:
    print('your number is too low')
else:
    print('your guess is too high')