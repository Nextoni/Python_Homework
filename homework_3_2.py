def count_words(arr):
    result = {}

    for words in arr:
        if words not in result:
            result[words] = 1
        else:
            result[words] = result[words] + 1
            
    
    return result


print(count_words(["apple", "banana", "apple", "pie"]))