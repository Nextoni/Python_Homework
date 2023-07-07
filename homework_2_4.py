def is_int_palindrome(num):
    result = False
    res = ""
    nums = num
    my_list = []

    for itr in range(num):
        my_list.append(nums % 10)
        nums = nums // 10
        if nums == 0:
            break

    for numb in my_list:
        res = res + str(numb)
    res = int(res)

    if res == num:
        result = True
    else:
        result = False

    return result

print(is_int_palindrome(5445))