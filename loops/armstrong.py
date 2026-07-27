def is_armstrong(n):
    original = n
    result = 0
    while n > 0:
        last = n % 10
        result += (last ** 3)
        n //= 10
    return result == original
print(is_armstrong(153))
