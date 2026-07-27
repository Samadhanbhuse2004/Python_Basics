def my_func(n):
    return lambda a: a*n
my_double = my_func(5)
print(my_double(2))