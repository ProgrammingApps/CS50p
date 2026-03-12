"""
Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein X is a non-negative integer and Y is a positive integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

"""

#X is a non-negative integer
#Y is a positive integer
#Output as a percentage rounded to the nearest integer
#1% or less output E
#99% or more output full.

def main():
    final_fuel = str(fuel())
    if final_fuel.isalpha():
        print(final_fuel)
    else:
        print(str(final_fuel) + "%")

def fuel():
    while True:
        try:
            numerator, denominator = input("Fraction: ").split('/')
            numerator = int(numerator)
            denominator = int(denominator)
            if denominator < numerator or numerator < 0:
                print("Invalid fuel inserted.")
                continue
            percentage = round(((numerator / denominator)*100))
        except (ValueError, ZeroDivisionError):
            print("Invalid fuel inserted.")
        else:
            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return("F")
            else:
                return(percentage)

main()
