values = [50, 34, 60, 90, 87, 33]


def square(v):
    return v * v


for v in map(square, values):
    print(v)
