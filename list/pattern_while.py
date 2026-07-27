i = 1
while i <= 5:
    k = 1
    while k < 6-i:
        print(' ', end=' ')
        k += 1
    j=1 
    while j <= i:
        j += 1
        print('*', end=' ')
    i += 1
    print()