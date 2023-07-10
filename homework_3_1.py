def is_anagram(first_word, second_word):
    first_word.lower()
    second_word.lower()
    result = True

    if len(first_word) != len(second_word):
        result = False

    for first in first_word:
        if second_word.__contains__(first) == False:
            result = False
            break
    
    return result

print(is_anagram("asd", "sdae"))

def is_anagram1(first_word, second_word):

    def sort_alg(my_string):
        my_string_res = []

        for char in my_string:
            my_string_res += char
        
        my_string_res.sort()

        return my_string_res

    first_word.lower()
    second_word.lower()
    result = True
    first_res = sort_alg(first_word)
    second_res = sort_alg(second_word)

    if first_res != second_res:
        result = False

    return result

print(is_anagram1("asd", "sda"))

