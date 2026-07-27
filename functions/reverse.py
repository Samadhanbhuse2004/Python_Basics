num = 12345
def reverse(num):
    result =0
    while num>0:
        last = num%10
        result = result*10+last
        num//=10
    return result
print(reverse(num))