def fruits(*args):
    return f'the favorite fruits is : {args[2]}'
    for i in fruits:
        print(i)
print(fruits('apple', 'banana', 'orange', 'grape'))