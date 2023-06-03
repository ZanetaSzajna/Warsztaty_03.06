import csv

def generate_mail(name_surname, missing_tasks,grades,date):
    for i in range(len(name_surname)):
        potential_grade = int(grades[i]) + 1
        zrodlo = open('emial.txt',encoding='1250').readlines()
        cel = open(f'emiall{i}.txt', 'w', encoding='1250')
        for s in zrodlo:
            cel.write(s.replace("[insert student name]", name_surname[i]).replace("[insert number of missing tasks]", missing_tasks[i]).replace("[insert current grade]", grades[i]).replace("[insert potential grade]", str(potential_grade)).replace("[insert one date for all students]", date))
        cel.close()
def main():
    name_surname = []
    missing_tasks = []
    grades = []
    date = "29.06.2023"
    with open("lista.csv") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=";")
        for row in csvreader:
            name_surname.append(row[1] + row[2])
            missing_tasks.append(row[3])
            grades.append(row[4])
    generate_mail(name_surname, missing_tasks,grades,date)
if __name__ == "__main__":
   main()