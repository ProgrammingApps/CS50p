'''
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns 
that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

def main():
    ...


def shorten(word):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, 
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_twttr.py
Hints
Be sure to include
import twttr
or

from twttr import shorten
atop test_twttr.py so that you can call shorten in your tests.

Take care to return, not print, a str in shorten. Only main should call print.
'''


'''
OLD CODE

#The task is to remove all vowels from strings.
#So first we need an "Input:" which will then take it and print an output.

def main():
    input_sentence = input("Input:")
    output = remove_vowels(input_sentence)
    print(output)

def remove_vowels(input_sentence):
    removed_vowels = ""
    for letter in input_sentence:
        if letter not in ["a", "A", "e", "E", "i", "I", "O", "o", "u", "U"]:
            removed_vowels = removed_vowels + letter
    return removed_vowels

main()

'''

def main():
    word = input("Input: ")
    output = shorten(word)
    print(output)


def shorten(word):
    removed_vowels = ""
    for letter in word:
        if letter not in ["a", "A", "e", "E", "i", "I", "O", "o", "u", "U"]:
            removed_vowels = removed_vowels + letter
    return removed_vowels


if __name__ == "__main__":
    main()