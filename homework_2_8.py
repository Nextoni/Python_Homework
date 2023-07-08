def biggest_difference(arr):
    result = 0
    arr.sort()
    print(arr)
    min_arr = arr[0]
    max_arr = arr[-1]

    result = min_arr - max_arr
    return result

print(biggest_difference([1, 2, 6, 4, 5]))