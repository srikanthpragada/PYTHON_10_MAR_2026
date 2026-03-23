data = [(1, 56), (1, 70), (2, 70), (2, 45), (4, 45), (3, 60)]

students = {}
for rollno, marks in data:
    total = students.get(rollno, 0)
    total += marks
    students[rollno] = total

for rollno, total in sorted(students.items()):
    print(rollno, total)
