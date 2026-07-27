def cube(func):
    def wrapper(*args):
        return func(*args) ** 3
    return wrapper

@cube
def square(n):
    return n
print(square(2))