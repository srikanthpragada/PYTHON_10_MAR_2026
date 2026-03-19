# Accept 2 strings and display the common characters

s1 = "java"
s2 = "kava"

found = False
found_chars = []
for c in s1:
    if c in s2 and c not in found_chars:
        found = True
        print(c, end=' ')
        found_chars.append(c)

if not found:
    print('No common chars!')
