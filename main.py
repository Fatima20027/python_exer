import random
def guess_the_number():
    number = random.randint(1, 100)
    i = 0
    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number")
            continue
        
        i += 1

        if guess < number:
            print ("too low, try again.")
        elif guess > number:
            print("too high, try again.")

        else:
            print(f"Congratualation! you guessed the number {number} in {i} attempts correctly!")
            return
guess_the_number()
