"""
One of David’s first toys as a child, funny enough, was Little Professor, 
a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to
 display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5.
If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, 
the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

In a file called professor.py, implement a program that:

Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits. 
No need to support operations other than addition (+).
Note: The order in which you generate x and y matters. 
Your program should generate random numbers in x, y pairs to simulate generating one math question at a time 
(e.g., x0 with y0, x1 with y1, and so on).

Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), 
the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. 
If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) 
the user for a level and returns 1, 2, or 3, and generate_integer returns a single randomly generated non-negative integer 
with level digits or raises a ValueError if level is not 1, 2, or 3:
"""
#Asks the user for a level
#The level determins how many digits in each problem.
#The problem will then generate a question, give them three tries. The programme with have 10 questions.
#The problem will output how many out of 10 are correct.

import random


def main():
    #Get the level
    level = get_level()
    #Loop 10 times for 10 questions
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        for j in range(3):
            #Ask the question
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                continue
                #Check the answer
            if answer == (x + y):
                score = score + 1
                break
            else:
                if j == 2:
                    real_answer = x + y 
                    print(f"{x} + {y} = {x + y}")
                    break
                print("EEE")
            #If all 3 tries used — show the answer
    print(score)
            

    #Inside that, generate x and y
    #Loop up to 3 times for attempts
    #Track the score


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()