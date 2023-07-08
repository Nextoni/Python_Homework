def count_substrings(haystack, needle):
    result = 0

    for itr in range(haystack.count(needle)):
        if haystack.count(needle):
            result = result + 1
        
    return result

print(count_substrings("Python is an awesome language to program in!", "o"))