import random
def number_guessing():
    n = random.randrange(1, 100)
    guess = int(input("Enter any number: "))
    attempts = 0
    
    while n != guess:
        if guess < n:
            print("Too low")
            guess = int(input("Enter number again: "))
        elif guess > n:
            print("Too high!")
            guess = int(input("Enter number again: "))
            attempts += 1

            print("You guessed it right!!")
            attempts += 1
            print("Number of attempts:", attempts)
number_guessing()