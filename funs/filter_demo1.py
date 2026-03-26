marks_list = [50, 34, 60, 90, 87, 33]


def is_passed(marks):
    return marks >= 50


for v in filter(is_passed, marks_list):
    print(v)
