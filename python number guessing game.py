import random
print('welcome to the number guessing game.\nyou have 7 chances to guess the number. lets start!')

low = int(input("enter the lower bound number: "))
high = int(input("enter the upper bound number: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low,high)
ch = 7
gc = 0

while gc < ch:
    gc=gc+1
    guess=int(input("enter your guess: "))

    if guess == num:
        print(f"congratulations! the number was {num} and you guesses it in {gc} attempts")
        break
    
    elif gc >= ch and guess!= num:
        print(f"the correct answer was {num}. better luck next time!")

    elif guess> num:
        print("guess is too high. try again.")
    
    elif guess < num:
        print("guess is too low. try again.")   