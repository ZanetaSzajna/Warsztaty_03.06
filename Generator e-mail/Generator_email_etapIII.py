import csv

name_surname = []
missing_tasks = []
grades = []
date="29.06.2023"
with open("lista.csv") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=";")
    for row in csvreader:
        name_surname.append(row[1]+row[2])
        missing_tasks.append(row[3])
        grades.append(row[4])



for i in range(len(name_surname)):
    potential_grade=int(grades[i])+1
    print(f"Welcome {name_surname[i]},\n This is a kindly reminder that you have {missing_tasks[i]} tasks left to submit before you can graduate.\n"
          f"Your current grade is {grades[i]} and can increase to {potential_grade} if you submit all assignments before the due date {date}.")


