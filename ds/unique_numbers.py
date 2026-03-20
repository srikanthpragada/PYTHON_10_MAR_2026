# Print unique numbers from the list in the order they appear
nums = [2,4,2,5,2,1,3,6]

unums = []
for n in nums:
    if n not in unums:
        unums.append(n)

print(unums)