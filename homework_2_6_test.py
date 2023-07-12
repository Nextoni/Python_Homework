def contains_digits(number, digits):
    result = True
    temp = []

    for itr in range(number):
        if number != 0:
            temp.append(number % 10)
            number = number // 10
    
    for iter in digits:
        if iter not in temp:
            result = False

    return result

print(contains_digits(1234, [1, 2, 3, 4]))