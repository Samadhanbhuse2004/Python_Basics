def is_armstrong_number(num):
    digit = 0
    temp = num
    while temp > 0:
        digit += 1
        temp //= 10
        temp = num
        sum_of_powers = 0
        while temp > 0:
            digit_value = temp % 10
            sum_of_powers += digit_value ** digit
            temp //= 10
    return num == sum_of_powers
