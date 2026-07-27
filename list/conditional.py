num = 0
while num <= 21:
    num += 1 
    if num == 3:  
        continue
    elif num == 10:
        pass
    elif num == 19:
        break
    print(f'current num: {num}')