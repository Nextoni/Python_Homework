def contains_digits(number, digits):
    result = True
    number = str(number)

    for itr in digits:
        if (number.count(str(itr)) == 0):
            result = False
            break

    return result

print(contains_digits(123, [1, 2, 3]))