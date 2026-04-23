def solution(digits):
    number = 0
    lst = []
    while number < len(digits):
        lst.append(int(digits[number:number+5]))
        number += 1
    return max(lst)