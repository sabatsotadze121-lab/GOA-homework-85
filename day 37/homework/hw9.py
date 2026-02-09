def even_numbers(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result

print(even_numbers([1, 2, 3, 4, 6, 7]))