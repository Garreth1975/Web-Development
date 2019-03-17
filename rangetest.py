import random
sn=random.randint(1,20)
print("I am thinking of a number between 1 and 20")

for guesstaken in range(1, 7):
    print("take a guess")
    guess = int(input())

    if guess < secretnumber:
        print("your number is too low.")
    elif guess > secretnumber:
        print("your guess is too high.")



    