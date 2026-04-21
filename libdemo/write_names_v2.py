
names = ['Scott', 'Dave', 'Marshall', 'Kevin', 'Bruse']

with open("names.txt", "wt") as f:
    for name in names:
        f.write(name + "\n")

