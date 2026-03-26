def calculate(n1, n2, task):
    print(task(n1, n2))


def add(a, b):
    return a + b

calculate(10, 20, add)
#calculate(10, 20, abs)

