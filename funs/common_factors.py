def common_factors(n1, n2):
    smallest = min(n1, n2)
    for i in range(2, smallest // 2 + 1):
        if n1 % i == 0 and n2 % i == 0:
            print(i, end = ' ')


common_factors(20, 40)