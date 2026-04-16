a = 10
b = 0

try:
    c = a / b
    print(c)
except ValueError as e:
    print(e)
finally:
    print('Finally!')

print('Done')
