def first_digit_pos(st):
    for idx, c in enumerate(st):
        if c.isdigit():
            return idx

    return -1


print(first_digit_pos('iPhone 17'))
print(first_digit_pos('iPad  Air'))
