def sum_of_divisors(num):
    result = 0

    for itr in range(1, num + 1):
        if (num % itr) == 0:
            result += itr
    
    return result

print(sum_of_divisors(8))