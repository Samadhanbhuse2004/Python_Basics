def Multi_sum(a,b):
    product = a*b
    if product <= 1000:
        return f"The product of a and b is less than or equal to 1000 : {product} "
    else:
        return f"The product of a and b is greater than 1000 : {a + b} "
    
print(Multi_sum(20,80)) 