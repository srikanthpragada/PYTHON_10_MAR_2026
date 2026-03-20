# print idex and value from a list

l = [10, 5, 20, 30, 15]

# idx  = 0
# for n in l:
#     print(idx, n)
#     idx += 1


for i, v in enumerate(l, start = 1):
    print(i, v)

