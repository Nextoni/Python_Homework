def contains_digits(number, digits):
    result = False
    number = str(number)
    digits = str(digits)

    for itr in range(0, len(number)):
        for iter in range(0, len(digits)):
            if number[itr] != digits[iter]:
                result = False
            elif number[itr] == digits[iter]:
                result = True
                break

    return result

print(contains_digits(123, [1, 2, 3]))