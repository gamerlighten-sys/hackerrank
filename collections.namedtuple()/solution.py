# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

N = int(input())
Student = namedtuple('Student', ["ID", "NAME", "MARKS", "CLASS"])

students = []
field = input().split()

for i in range(N):
    student_input = input().split()
    student_data = {}
    
    for j in range(4):
        student_data[field[j].upper()] = student_input[j]

    student = Student(**student_data)
    students.append(student)
    
final_sum = 0
for student in students:
    final_sum += int(student.MARKS)

avg = float(final_sum) / len(students)

print(avg)