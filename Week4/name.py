import sys

if len(sys.argv) <= 1:
    sys.exit("Too few values")
elif len(sys.argv) > 2:
    sys.exit("Too many values")

print("Hello, my name is", sys.argv[1])