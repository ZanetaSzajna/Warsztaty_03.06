#Etap I

name=input("Please enter names separate space--> ")
last_name=input("Please neter separate space-->  ")
missing_tasks=input("how many tasks are missing -->  ")
grade=input("Enter grade --> ")
date="29.06.2023"
list_name=list(name.split())
list_last_name=list(last_name.split())
list_tasks=list(missing_tasks.split())
list_grade=list(grade.split())

print(list_name)
print(list_tasks)
print(list_last_name)
print(list_grade)


for i in range(len(list_name)):
    potential_grade=int(list_grade[i])+1
    print(f"Welcome {list_name[i]} {list_last_name[i]},\n This is a kindly reminder that you have {list_tasks[i]} tasks left to submit before you can graduate.\n"
          f"Your current grade is {list_grade[i]} and can increase to {potential_grade}\n "
          f"if you submit all assignments before the due date {date}.")