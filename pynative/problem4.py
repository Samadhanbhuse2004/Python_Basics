def is_prime(num):
    if num <= 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
    return True
print(is_prime(6)) 
print(is_prime(23))  
print(is_prime(24))  
print(is_prime(37))  
print(is_prime(62))     