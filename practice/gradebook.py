'''
Gradebook  (Week 6: csv.DictReader, csv.DictWriter, writeheader, file errors)

This is the warm-up for scourgify.py: same skills, different data.

Goal: read a CSV of scores and write a new CSV with a grade column added.

    python gradebook.py grades.csv report.csv

Steps:

Expect exactly two command-line arguments: an input CSV and an output CSV.
Exit via sys.exit with a message if the argument count is wrong or the input can't be read.
grades.csv has columns: name, score
Write report.csv with columns, in order: name, score, grade
Grades: 70+ → A, 60–69 → B, 50–59 → C, below 50 → F
If a score isn't a number (e.g. "absent"), don't write that row. Instead print a
warning to the terminal:  Skipping Dev: score "absent" is not a number
Finally print the class average of the valid scores to one decimal place.

Self-check (with the grades.csv provided):

Terminal:
    Skipping Dev: score "absent" is not a number
    Class average: 68.1

report.csv should start:
    name,score,grade
    Ada,82,A
    Brian,67,B
    Chloe,49,F

Reflect: what does writeheader() write, and where does DictWriter get it from?
'''
