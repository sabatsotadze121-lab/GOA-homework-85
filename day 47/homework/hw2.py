def letter_count(string):
    result = {}
    
    for c in string:
        if c in result:
            result[c] += 1
        
        else:
            result[c] = 1
    
    return result


def is_anagram(test, original):
    count_test = letter_count(test.lower())
    
    for c in original.lower():
        try:
            count_test[c] -= 1
        except KeyError:
            return False

    for i in count_test:
        if count_test[i]:
            return False
    
    return True