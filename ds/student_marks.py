data = [(1, 56), (1, 70), (2, 70), (2, 45), (4, 45), (3, 60)]

students = {}
for rollno, marks in data:
    marks_list = students.get(rollno, [])
    marks_list.append(marks)
    students[rollno] = marks_list

for rollno, marks_list in sorted(students.items()):
    print(rollno, marks_list)
