import sys

if len(sys.argv) < 2:
    print('Sorry! Number is missing!')
    exit()

for num in map(int, filter(str.isdigit, sys.argv[1:])):
    print(f'{num} -> ', end='')
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            print(i, end=' ')

    print()  # next line
