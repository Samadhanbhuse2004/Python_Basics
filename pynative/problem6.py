previous_num = 0
for i in range(10):
    sum = previous_num + i
    print(f"Current_number: {i} previous_number: {previous_num} Sum: {sum}")
    previous_num = i