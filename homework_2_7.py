def count_substrings(haystack, needle):
    result = 0

    for itr in range(haystack.count(needle)):
        if haystack.count(needle):
            result = result + 1
        
    return result

print(count_substrings("babababa", "baba"))



def count_substrings1(haystack, needle):
    result = 0

    for char in range(len(haystack)):
        if haystack[char : char + len(needle)] == needle:
            result += 1

    return result

print(count_substrings1("babababa", "baba"))