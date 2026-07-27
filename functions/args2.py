def get_sum(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print(get_sum(1,2,3,4,5,6,7,8,9,10))