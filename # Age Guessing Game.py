# Age Guessing Game

low = 1
high = 100
attempts = 0

print("Think of your age (between 1 and 100).")
input("Press Enter when ready...")

while low < high:
    guess = (low + high) // 2
    answer = input(f"Is your age greater than {guess}? (y/n): ").lower()
    attempts += 1
    if answer == 'y':
        low = guess + 1
    elif answer == 'n':
        high = guess
    else:
        print("Please enter 'y' or 'n'.")

print(f"Your age is {low}! I guessed it in {attempts} questions.")