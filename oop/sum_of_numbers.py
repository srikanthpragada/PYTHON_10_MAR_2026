
total = 0

while True:
    try:
        num = int(input("Enter number [0 to stop] :"))
        if num == 0:
            break
        total += num
    except ValueError as e:
        print('Error: ', e)
    except ZeroDivisionError as e:
        print(e)

print("Total:", total)

