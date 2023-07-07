def contains_digit(number, digit):
    result = False
    strin = [int(iter) for iter in str(number)]

    for itr in strin:
        if digit == itr:
            result = True
            break
        else:
            result = False
    return result

print(contains_digit(1234, 2))
