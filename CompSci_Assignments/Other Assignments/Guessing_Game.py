import random

answer = random.randrange(1, 101)

print("Welcome to the guessing game.")
print("Try to guess the number between 1 and 100.")

count = 0
guess = -1

while guess != answer:
    guess = int(input("Guess a number. "))
    count += 1
    if int(guess) > answer:
        print("To High")
    elif int(guess) < answer:
        print("To Low")
    else:
        print("Correct")

if count == 1:
    print("It took you", count, "guess")
else:
    print("It took you", count, "guesses")
