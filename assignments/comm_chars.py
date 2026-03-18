# Accept 2 strings and display the common characters

s1 = input("Enter string 1 : ")
s2 = input("Enter string 2 : ")
found = False
for c in s1:
    if c in s2:
        found = True
        print(c, end=' ')

if not found:
    print('No common chars!')
