
'''
Write a program in which you define a student name and his grades: Mathematics, Chemistry,
Physics, Biology, Informathics
Calculate the average of the grades and print this message:  The average of the grades of
{student_name} is {average}
The name of the student and the average should be individual variables and printed using output formatting
'''


student_name = "Alexander"

math = 8.5
chemistry = 8
physics = 9.2
biology = 9.3
info = 9.1


def calculate_average(note1, note2, note3, note4, note5):
    return (note1 + note2 + note3 + note4 + note5) / 5

print(f"The average of the grades of {student_name} is {calculate_average(math, chemistry, physics, biology, info)}")