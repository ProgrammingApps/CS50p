"""

x = 0

while x < 3:
    print("Meow")
    x += 1



for  i in range(3)  :
    print("meow")

    
We can also use multiply!:

print("Meow\n" * 3, end="")

while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break

for _ in range(n):
    print("Meow")

#can also just use break without continue, so if n > 0: break. The code above will keep asking what's n until it's positive.
"""
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        number = int(input("What number are you thinking of?"))
        if number > 0:
            return number

def meow(n):
    for _ in range(n):
        print("Meow")

main()
    