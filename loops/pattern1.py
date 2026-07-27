rows = 5
for i in range(rows + 1):
    if i == rows:
        for j in range(rows + 1):
            print("*", end=" ")
    else:
        for j in range(i + 1):
            if j == 0 or j == i:
                print("*", end=" ")
            else:
                print(" ", end=" ") 
    print()