def reverse_string(s):
    l = len(s)
    rev = ''
    while l > 0:
        rev += s[l - 1]
        l -= 1
    return rev
print(reverse_string("python"))