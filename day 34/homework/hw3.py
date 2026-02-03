def sum_of_even_elements():
    numbers = [2, 5, 8, 11, 14, 7, 6]
    total = 0

    for num in numbers:
        if num % 2 == 0:
            total += num

    print("ლუწი ელემენტების ჯამია:", total)

sum_of_even_elements()