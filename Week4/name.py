import sys

if len(sys.argv) <= 1:
    sys.exit("Too few values")

for arg in sys.argv[1:]:
    print(f"Hello, my name is {arg}")
