def sum_of_minimums(numbers):
    summ = 0
    for i in range(len(numbers)):
        summ = summ + min(numbers[i])
    return summ