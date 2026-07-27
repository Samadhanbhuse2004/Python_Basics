i = 1
n = 5
while i <= n:
    j = 1
    while j <=n-i:
        print(' ', end=' ')
        j += 1     

    k = 1
    while k <= 2*i - 1:
        print('*', end=' ')
        k += 1

    i += 1
    print()