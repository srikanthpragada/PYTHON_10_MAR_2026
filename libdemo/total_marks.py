f = open('marks.txt', "rt")

for line in f.readlines():
    parts = line.split(",")
    name = parts[0]
    marks = parts[1:]
    total = sum(map(int, marks))
    print(f"{name} - {total}")

f.close()
