def sum_of_numbers(strin):
    result = 0
    temp = ""

    for itr in strin:
        if itr.isdigit() == True:
            temp = str(temp) + itr
        elif itr.isdigit() == False:
            result += int(temp)
            temp = 0
           
    return result

print(sum_of_numbers("56abc444a"))