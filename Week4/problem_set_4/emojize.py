#In a file called emojize.py, implement a program that prompts the user 
# for a str in English and then outputs the “emojized” version of that str,
#converting any codes (or aliases) therein to their corresponding emoji.
import emoji

def main():
    emoji_creator()

def emoji_creator():
    response = input("Input: ")
    print(emoji.emojize(response))


main()
