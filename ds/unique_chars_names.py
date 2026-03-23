
names  = ['Anders', 'Scott', 'Mark', 'Jack', 'Jo']

uchars = set()

for name in names:
    uchars = uchars | set(name)

print( sorted(uchars))
