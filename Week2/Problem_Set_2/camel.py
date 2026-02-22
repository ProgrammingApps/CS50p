
def main():
    name = input("camelCase:")
    for letter in name:
        if letter.isupper():
            print("_", end = "")
            print(letter.lower(), end = "")
        else:
            print(letter, end = "")
    

main()