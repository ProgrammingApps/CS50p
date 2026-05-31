'''
Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its menu too, per this CSV file of Sicilian pizzas, sicilian.csv, below:

Sicilian Pizza,Small,Large
Cheese,$25.50,$39.95
1 item,$27.50,$41.95
2 items,$29.50,$43.95
3 items,$31.50,$45.95
Special,$33.50,$47.95
See regular.csv for a CSV file of regular pizzas as well.

Of course, a CSV file isn’t the most customer-friendly format to look at. Prettier might be a table, formatted as ASCII art, like this one:

+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+
In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, 
and outputs a table formatted as ASCII art using tabulate, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. 
If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist, 
the program should instead exit via sys.exit.
'''

#Expecting python pizza.py (Then regular or sicillian)
#It will then print out in ASCII form the menu.
#Error handling: one command-line argument, must end in .csv - changed this so that it just adds .csv, file does not exist, exists in sys.exit.

import csv
import sys
from tabulate import tabulate

def main():
        try:
            if len(sys.argv) != 2:
                 sys.exit("Expecting two filenames")
            filename = sys.argv[1]
            if not filename.endswith(".csv"):
                sys.exit("Must end with .csv")
                filename = sys.argv[1] + ".csv"
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                print(tabulate(reader, headers="keys", tablefmt="grid"))
        except FileNotFoundError:
             sys.exit("Sorry, the file you're looking for does not exist!")


if __name__ == "__main__":
    main()