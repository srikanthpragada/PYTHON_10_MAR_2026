# Display avg for either 5 numbers or until 0 is given

total = count =  0
for n in range(5):
    num = int(input("Enter a number [0 to stop] :"))
    if num == 0:
        break
    total += num
    count += 1

print(f'Average = {total // count}')
