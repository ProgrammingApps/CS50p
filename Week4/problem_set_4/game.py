"""
I’m thinking of a number between 1 and 100…

What is it?
In a file called game.py, implement a program that:

Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.

Takes a level input
Then randomises a number between that number input and 1
then takes another input, guess.
If less then (too low)
if more than (too high)
if equal to (just right)
Needs to be a while true loop that exits when it hits equal.


import random

random.randint(1, 10)    # random integer between 1 and 10 inclusive
random.choice(["a", "b", "c"])  # picks a random item from a list


Now just need to handle errors.
Need to handle ctrl d error
error if it's a negative input.
error if it's not a number.
tends to be with the "try" command. 
"""

import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level < 1:
                continue
        except ValueError:
            continue
        except EOFError:
            print("Game exited")
            sys.exit()
        break

    choice = random.randint(1, level)
    while True:
            try:
                guess = int(input("Guess: "))
                if guess < 1:
                    continue
                if guess < choice:
                    print("Too small!")
                if guess > choice:
                    print("Too large!")
                if guess == choice:
                    print("Just right!")
                    break
            except ValueError:
                continue
            except EOFError:
                print("Game exited")
                sys.exit()

main()
