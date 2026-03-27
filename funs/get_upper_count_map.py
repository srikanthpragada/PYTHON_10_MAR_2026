def count_upper(st : str) -> int:
    count = 0
    for c in st:
        if c.isupper():
            count += 1

    return (st, count)

names = ['Java', 'Python', 'C', 'SQL', 'javascript', 'Php']

for name, count in map(count_upper, names):
    print(name, count)
