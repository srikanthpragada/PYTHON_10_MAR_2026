import re

with open("customers.txt", "rt") as f:
    for line in f.readlines():
        # take name
        m = re.search('[a-zA-Z]+', line)
        name = m.group()

        # take mobile
        m = re.search(r'\d{5,}', line)
        if m is not None:
            print(f"{name:15} {m.group()}")



