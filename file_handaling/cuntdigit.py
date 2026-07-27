def count_digit(n):
    if n<=0:
        return 0
    ans = 1+ count_digit(n//10)
    return ans
print(count_digit(1234))