def count_factors(num):
    count = 0
    for n in range(2, num//2 + 1):
        if num % n == 0:
            count += 1

    return count

c = count_factors(2556)
print(c)
