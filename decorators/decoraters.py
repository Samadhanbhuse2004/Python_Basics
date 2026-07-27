def my_decorator(f):
    def wrapper():
        return "Hello " + f() + " How are you ?"
    return wrapper

@my_decorator
def my_intro():
    return "Samadhan "
print(my_intro())