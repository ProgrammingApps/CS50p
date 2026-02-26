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