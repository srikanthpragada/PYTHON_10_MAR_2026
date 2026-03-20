# Display all unique chars from given names

names = ['Andy', 'Marshall', 'Ben', 'Mark']

chars = []
for name in names:
    for c in name:
        if c not in chars:
            chars.append(c)

print(chars)
