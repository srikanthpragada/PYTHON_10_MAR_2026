# Take a string and print sum of codes

st = input("Enter my string : ")

total = 0
for c in st:
    total += ord(c)

print(total)
