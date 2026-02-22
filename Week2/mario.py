"""
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")



main()



def main():
    print_row(4)

def print_row(question_mark):
    print("?" * question_mark)


main()



def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()

"""

def main():
    print_square(3)

def print_square(size):

    for i in range(size):

        for j in range(size):
            print("#", end="")
        
        print()

main()