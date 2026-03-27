marks = "98,45,88,33,aa,45"

valid_marks = filter(str.isdigit, marks.split(","))
total = sum(map(int, valid_marks))
print(total)

