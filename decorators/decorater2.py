def remove_last(func):
    def wrapper(*args):
        result = func(*args)//10
        return result
    return wrapper

@remove_last
def num(n):
    return n
print(num(345))