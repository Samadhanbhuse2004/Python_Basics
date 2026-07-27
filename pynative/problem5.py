def multiplication(a,b):
    product = a*b
    if product <= 1000:
        return product
    else:
        return a+b
result = multiplication(20,23)
print("The result is : " , result)
result = multiplication(80,90)
print("The result is : " , result)