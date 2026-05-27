'''
names = []

for _ in range(3):
    name = input("What's your name? ")
    names.append(name)

#names.sort()
#for i in names:
   # print(i)

for name in sorted(names):
    print(f"Hello, {name}")




name = input("What's your name? ")

file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()


with open("names.txt", "a") as file:
    file.write(f"{name}\n")

 
with open("names.txt", "r") as file:
    for line in file:
        print(f"Hello, {line.strip()}",)



names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())
    
for name in sorted(names):
    print(f"Hello, {name}")


with open("names.txt") as file:
    for line in sorted(file):
        print(f"Hello, {line.rstrip()}")

'''


names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())
    
for name in sorted(names, reverse=True):
    print(f"Hello, {name}")
