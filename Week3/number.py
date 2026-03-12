
def main():
    x = get_int("What's x? ")
    print(f"X is {x}")

def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            pass
        else:
            break
    return x

main()