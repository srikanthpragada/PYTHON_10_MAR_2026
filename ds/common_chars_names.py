# Display all common chars among 5 names

names  = ['anders', 'andy', 'mark', 'jack', 'marshall']

uchars = set(names[0])

for name in names[1:]:
    uchars = uchars & set(name)

print( sorted(uchars))
