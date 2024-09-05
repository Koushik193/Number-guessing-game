import random

def display_welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    display_welcome_message()
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    attempts = 0
    guessed_correctly = False
    
    while not guessed_correctly:
        guess = get_user_guess()
        attempts += 1
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You've guessed the number {number_to_guess} correctly.")
            print(f"It took you {attempts} attempts to guess the number.")

if __name__ == "__main__":
    main()
