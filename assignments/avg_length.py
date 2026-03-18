# Take names until end is given and display avg length

total = count = 0

while True:
    name = input("Enter name [end to stop] :")
    if name.lower() == 'end':
        break

    count += 1
    total += len(name)

print(total / count)
