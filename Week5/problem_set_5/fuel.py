
#X is a non-negative integer
#Y is a positive integer
#Output as a percentage rounded to the nearest integer
#1% or less output E
#99% or more output full.
'''
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
'''
#God Damn gotta restrucutre this code.

def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            final_fuel = str(gauge(percentage))
            if final_fuel.isalpha():
                print(final_fuel)
                break
            else:
                print(str(final_fuel) + "%")
                break
        except (ValueError, ZeroDivisionError):
            print("Invalid fuel inserted.")
            continue


def convert(fraction):
        numerator, denominator = fraction.split('/')
        numerator = int(numerator)
        denominator = int(denominator)
        if denominator < numerator or numerator < 0:
            raise ValueError
        percentage = round(((numerator / denominator)*100))
        return percentage



def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return("F")
    else:
        return(percentage)


if __name__ == "__main__":
    main()


#Take aways; Nice changing things around, although, let's have the error handling done by main too. 