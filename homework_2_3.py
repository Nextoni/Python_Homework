def is_prime(num):
    result = False

    for itr in range(0, num):
        if itr == 0:
            continue
        if num % itr == 0 and itr != 1 and itr != num:
            result = False
            break
        else:
            result = True

    return result

print(is_prime(8))