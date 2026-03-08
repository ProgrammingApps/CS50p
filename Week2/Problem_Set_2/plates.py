"""
“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”

"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Check 1: starts with at least two letters
    if not s[0:2].isalpha():
        return False
    # Check 2: length between 2 and 6
    if not 2 <= len(s) <= 6:
        return False
    # Check 3: only letters and numbers (no punctuation/spaces)
    if not s.isalnum():
        return False
    # Check 4: numbers only at the end, and first number isn't '0'
    found_digit = False
    for letter in s:
        if letter.isdigit():
            if not found_digit:
                if letter == "0":
                    return False
            found_digit = True
        elif found_digit:
            return False
    return True
main()