'''
Dice  (Week 4: libraries, random, sys.argv, sys.exit)

Goal: a command-line dice roller using tabletop notation.

    python dice.py 3d6     → roll three six-sided dice

Steps:

Expect exactly one command-line argument in the form NdS:
  - N = number of dice, 1–10
  - S = sides, one of 4, 6, 8, 10, 12, 20
If anything is wrong (missing argument, too many, bad format, out of range),
exit via sys.exit with a helpful message, e.g. "Usage: python dice.py NdS (e.g. 3d6)".
Roll the dice with the random module and print:

    Rolls: 4, 1, 6
    Total: 11

Examples of invalid arguments: 3, d6, 3d7, 0d6, 11d6, 3x6, threed6

Reflect: you did sys.exit inside a try block in pizza.py. Why doesn't
"except FileNotFoundError" catch the SystemExit that sys.exit raises?
What would happen if you wrote a bare "except:"?

Stretch: support a modifier, e.g. 2d6+3 → add 3 to the total.
'''
