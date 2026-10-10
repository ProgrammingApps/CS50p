'''
Word frequency  (Week 6: reading files, with open, plus dicts and sorting)

Goal: find the most common words in a text file.

    python wordfreq.py words.txt

Steps:

Expect exactly one command-line argument: a file name ending in .txt.
Exit via sys.exit with a message if: wrong number of arguments, not .txt, or the file doesn't exist.
Count every word, case-insensitively, ignoring punctuation stuck to either end of the word
("Fine." and "fine" are the same word). The string module has something useful here.
Print the 5 most common words, most common first, as  word: count
If two words have the same count, put them in alphabetical order.

Self-check (with the words.txt provided):

the: 15
he: 8
and: 6
lamp: 4
was: 4

Hint for the tie-break: look up the key= parameter of sorted() from the Week 6 lecture.

Reflect: why use  with open(...)  instead of  open(...)  on its own?
'''
