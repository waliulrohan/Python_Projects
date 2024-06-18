import random

number = random.randint(1 ,100)
print(number)

guesses = 0

while True:
    try:
        userInput = int(input("Guess the number(1 - 100): "))
        if userInput >100 or userInput < 1:
            print("Guess a number between 1 and 100")
        else:
            guesses += 1
            if userInput > number:
                print('Too high! Try guessing a lower number.')
            elif userInput < number:
                print('Too low! Try guessing a higher number.')
            elif userInput == number:
                print(f"You guessed the number {number} in {guesses} guesses")
                break
    except ValueError:
        print("Guess a valid number betweeen 1 and hundred.")