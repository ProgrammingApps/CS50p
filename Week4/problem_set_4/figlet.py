"""
Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, 
and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
the program should exit via sys.exit with an error message.
"""
import sys
import pyfiglet
import random

def main():
    if len(sys.argv) == 1: #python pyfiglet.py - RANDOM FONT
        response = input("Input: ")
        style_choice = random.choice(pyfiglet.FigletFont.getFonts())
        f = pyfiglet.Figlet(font=style_choice)
        print(f.renderText(response))
    elif len(sys.argv) ==3: #python pyfiglet.py -f slant - SPECIFIC FONT
        if sys.argv[1] not in ["-f", "--font"]:
            sys.exit("Expecting either -f or --font for the first argument")
        if sys.argv[2] not in pyfiglet.FigletFont.getFonts():
            sys.exit("Invalid font")
        response = input("Input: ")
        f = pyfiglet.Figlet(font=sys.argv[2])
        print(f.renderText(response))
    else:
        sys.exit("Looking for either 1 or 3 arguments")

main()