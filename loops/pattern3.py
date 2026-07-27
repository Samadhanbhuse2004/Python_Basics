for i in range(1,6):
    for j in range(5-i):
        print(' ', end=' ')
    for k in range(2*i-1):
        print('*', end=' ')
    print()    
    
rows = 4

for i in range(1, rows + 1):
    
    # Spaces for centering
    for s in range(rows - i):
        print(' ', end=' ')
    
    # Left side: i → a (decreasing)
    for j in range(i, 0, -1):
        print(chr(96 + j), end=' ')
    
    # Right side: b → i (increasing)
    for j in range(2, i + 1):
        print(chr(96 + j), end=' ')
    
    print()
    
    rows = 4

for i in range(1, rows + 1):
    
    # Spaces for alignment
    for s in range(rows - i):
        print(' ', end=' ')
    
    # Left side: i → 1 (decreasing)
    for j in range(i, 0, -1):
        print(j, end=' ')
    
    # Right side: 2 → i (increasing)
    for j in range(2, i + 1):
        print(j, end=' ')
    
    print()