def is_palindrome(n):
    reversed = 0
    original = n

    while n>0:
        last = n%10
        reversed = reversed*10+last
        n//=10
    
    return reversed == original

print(is_palindrome(121))

def is_palindrome_pointer(n):
    s = str(n)
    left = 0
    right = len(str(n))-1

    while left<right:
        if s[left]!=s[right]:
            return False
        
        left +=1
        right-=1
    
    return True

print(is_palindrome_pointer(12321))