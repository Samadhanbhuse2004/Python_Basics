def largest_smallest_num(n):
    largest = 0
    smallest = 0
    while n > 0:
        digit = n%10
        if digit > largest:
            largest = digit
    return largest
print(largest_smallest_num(12345))
