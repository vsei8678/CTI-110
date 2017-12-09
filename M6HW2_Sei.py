
# November 12, 2017
# CTI-110
# M6HW2
# Vincent Sei

import random

Limit = 100

def showTitle():
    print("Guess the number!")
    print()
def play_game():
    number = random.randint(1, Limit)
    count = 1
    while True:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:
            print("Too high.")
            count += 1
        elif guess == number:
            
        
            print("It took you " +str(count) + " attempts to guess correctly.\n")
            return
def main():
    showTitle()
    again = "y"
    while again.lower() == "y":
        play_game()
        again = input("would you like to play again? (y/n): ")
        print()
        print("Bye!")
        
  
    
main()           
