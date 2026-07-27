'''def reverse_num(n):
    reverse =0
    while n>0:
        last = n%10
        reverse = reverse*10+last
        n//=10
        return reverse   
print(reverse_num(1234))'''


def reversed_num(n):
    reverse = 0
    while n>0:
        last = n%10
        n//=10
        return reverse*10+last
print(reversed_num(10234))