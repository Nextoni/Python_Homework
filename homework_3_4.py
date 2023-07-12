def group(arr):
    result = []
    temp = []

    for n in arr:
        if temp == []:
            temp.append(n)
        else:
            if n in temp:
                temp.append(n)
            else:
                result.append(temp)
                temp = []
                temp.append(n)

    result.append(temp)
    
    return result

print(group([1, 1, 1, 1, 2, 2, 2, 3, 3, 3]))

def max_consecutive(items):

    result = []
    temp = []
    res_num = 0

    for n in items:
        if temp == []:
            temp.append(n)
        else:
            if n in temp:
                temp.append(n)
            else:
                result.append(temp)
                temp = []
                temp.append(n)

    result.append(temp)

    for n in result:
        if res_num < len(n):
            res_num = len(n)

    return res_num

print(max_consecutive([1, 1, 1, 1, 2, 2, 2, 3, 3, 3]))

