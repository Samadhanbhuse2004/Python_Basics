i = 1
while i <= 5:
    k=1 
    while k <= 5:
        if k==3:
            print('*', end=' ')
        elif i==3:
            print('*', end=' ')
        else:
            print(' ', end=' ')
        k+=1
    i += 1
    print()