
names = ['Scott', 'Dave', 'Marshall', 'Kevin', 'Bruse']

f = open("names.txt", "wt")

for name in names:
    f.write(name + "\n")

f.close()
