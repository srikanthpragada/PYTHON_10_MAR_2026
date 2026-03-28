d = {1 : 'abc', 2 : 'pqr', 3 : 'def', 4 : 'aaa'}

for t in sorted(d.items(), key =  lambda t : t[1]):
    print(t)

