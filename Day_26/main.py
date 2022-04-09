# LIST COMPREHENSION

# list = [1,2,3]
# new_list = [n+1 for n in list]

name = "angela"
name_alphabet = [letter for letter in name]
#print(name_alphabet)

new_number = [n * 2 for n in range(1, 5)]
#print(new_number)

# LIST COMPREHENSION CONDITION
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_name = [name for name in names if len(name)<= 4]
#print(short_name)

upper_case_long_name = [name.upper() for name in names if len(name) > 4]
#print(upper_case_long_name)


# DICTIONARY COMPREHENSION CONDITION
# new_dict = {new key : new value for (key,value) in dict.items if test}
# import random
# students_score = {student: random.randint(1,100) for student in names}
# print(students_score)
# passed_student = {student: score for (student, score) in students_score.items() if score > 60}
# print(passed_student)

#LOOP THROUGH PANDAS DATA FRAME
student_dict = {
    "students": ["Angela", "James", "Anna"],
    "scores": [70, 90, 60]
}
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.students)
    if row.students == "Angela":
        print(row.scores)