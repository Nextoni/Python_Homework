def sum_of_max_and_min(seq):
    result_min = seq[0]
    result_max = 0
    result = 0
    
    for nums in seq:
        if result_max < nums:
            result_max = nums
        if result_min > nums:
            result_min = nums
    
    result = result_max + result_min
    return result

print(sum_of_max_and_min([7, 6, 10, 2]))