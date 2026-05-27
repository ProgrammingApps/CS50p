import csv

'''
students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:     #alternatively for name, enjoys
        students.append({"name": row[0], "enjoys": row[1]}) #then it would be "name": name, "enjoys": enjoys

#def get_name(student):    (student): == student:
    #return student['name'] student['name'] == student['name']


for student in sorted(students, key=lambda student: student['name'], reverse= True):
print(f"{student['name']} really enjoys {student['enjoys']}")

'''

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:     #alternatively for name, enjoys
        students.append({"name": row["name"], "enjoys": row["enjoys"]}) #then it would be "name": name, "enjoys": enjoys

#def get_name(student):    (student): == student:
    #return student['name'] student['name'] == student['name']


for student in sorted(students, key=lambda student: student['name']):
    print(f"{student['name']} really enjoys {student['enjoys']}")