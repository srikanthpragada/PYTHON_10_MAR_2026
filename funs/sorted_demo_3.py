
names = ['  java', '  c++', 'Python', ' C', 'SQL  ', 'JavaScript   ']

for n in sorted(names, key = lambda s : s.strip().lower()):
    print(n)

