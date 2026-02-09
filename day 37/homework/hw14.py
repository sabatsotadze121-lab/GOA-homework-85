def sum_in_range(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

print(sum_in_range(5, 100))