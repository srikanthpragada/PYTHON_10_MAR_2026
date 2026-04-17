
total = 0
count = 0
while True:
    try:
        num = int(input("Enter number [0 to stop] :"))
        if num == 0:
            break
        total += num
        count += 1
    except ValueError as e:
        print('Error: ', e)


print("Total:", total)
print("Average :", total // count)

