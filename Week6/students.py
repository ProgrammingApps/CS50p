'''
with open("students.csv", "r") as file:
    for line in sorted(file):
        name, enjoys = line.rstrip().split(",")
        print(f"{name} is currently enjoying {enjoys}")


students = []

with open("students.csv") as file:
    for line in file:
        name, enjoys = line.rstrip().split(",")
        students.append(f"{name} is currently enjoying {enjoys}")

for student in sorted(students):
    print(student)



'''


students = []

with open("students.csv") as file:
    for line in file:
        name, enjoys = line.rstrip().split(",")
        student = {"name": name, "enjoys" : enjoys}
        students.append(student)

#def get_name(student):    (student): == student:
    #return student['name'] student['name'] == student['name']


for student in sorted(students, key=lambda student: student['name'], reverse= True):
    print(f"{student['name']} really enjoys {student['enjoys']}")
