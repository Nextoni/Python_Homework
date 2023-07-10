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

print(group([1, 1, 1, 2, 2, 3, 3]))