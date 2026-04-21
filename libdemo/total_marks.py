f = open('marks.txt', "rt")

for line in f.readlines():
    parts = line.strip().split(",")
    if len(parts) < 2:
        continue    # ignore line as it doesn't have enough data

    name = parts[0]
    marks = parts[1:]
    valid_marks = filter(str.isdigit, marks)
    total = sum(map(int, valid_marks))
    print(f"{name} - {total}")

f.close()
