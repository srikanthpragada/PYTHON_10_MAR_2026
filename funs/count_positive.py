
def count_positive(nums):
    count = 0
    for n in nums:
        if n > 0:
            count +=1

    return count

print( count_positive([-9,9,8,7,-4]))
