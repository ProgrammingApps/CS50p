"""
In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d.
Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names 
with two commas and one and, and 𝑛 names with 𝑛 −1 commas and one and, as in the below:

Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

Breakdown of problem logic:

control-d means we need to exit on an exit error (using a While True)
Needs to take an input and then keep storing each input. I wonder how to do that. Create list, append to list.

We ask for all their names.

Follow the gramatical rules when printing them out
inflect:
import inflect
p = inflect.engine()
p.join(["Liesl", "Friedrich", "Louisa"])
# returns "Liesl, Friedrich, and Louisa"
"""
import inflect

def main():
    names = []
    p = inflect.engine()
    while True:
        try:
            names.append(input("Name: "))
        except EOFError:
            break
    print(f"Adieu, adieu, to {p.join(names)}")


main()