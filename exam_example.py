'''
def img_rotate(arr):
    temp_arr = []

    for itr in arr:
        if arr[len(arr) / 2]:
            arr[len(arr) / 2].reverse()
    
    return temp_arr

print(img_rotate([[1, 0, 1], [0, 1, 1], [1, 0, 0]]))
'''

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

'''
def nokia_text(digits):
    chars = {0:' ', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
    result = ""
    digits = str(digits)
    temp = []

    for iter in digits:
        temp.append(int(iter))
    
    temp = group(temp)



    for itr in range(len(temp)):
        temp_count = temp[itr].count(temp[itr][0])
        for x in chars[temp_count]:
            result += x

    return result

print(nokia_text(7778822999))
'''
def numbers_to_msg(num):
    chars = {0:' ', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
    group = []
    temp_group = []
    for i in num:
        if temp_group == []:
            temp_group.append(i)
        elif i in temp_group:
            temp_group.append(i)
        else:
            if i > 0:
                group.append(temp_group)
                temp_group = []
                temp_group.append(i)
            else:
                temp_group.append(i)
    group.append(temp_group)

    result = ''

    for sub_group in group:
        char_pos = len(sub_group) % len(chars[sub_group[0]]) - 1
        result = result + chars[sub_group[0]][char_pos]

    return result


print(numbers_to_msg([6, 2, 7, 7, 7, 4, 4, 4, 9, 9, 9, 2, 6, 6]))

def nokia_text(digits):
    chars = {0:' ', 2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
    result = ""
    digits = str(digits)
    temp = []

    for iter in digits:
        temp.append(int(iter))
    
    temp = group(temp)

    result1 = ''

    for sub_group in temp:
        char_pos = len(sub_group) % len(chars[sub_group[0]]) - 1
        result = result + chars[sub_group[0]][char_pos]

    return result

print(nokia_text(62777444999266))