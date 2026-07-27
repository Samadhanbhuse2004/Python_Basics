for i in range(1,6):
    for j in range(i):
        if 0<i<4 and 0<j<3:
            print('#',end=' ')
        else:
            print('*',end=' ')
    print()    