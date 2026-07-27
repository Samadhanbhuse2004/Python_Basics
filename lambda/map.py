l1 = [1,2,3,4,5]
print(list(map(lambda x: x**2, l1)))

def square(n):
    return n**2
print(list(map(square, l1)))