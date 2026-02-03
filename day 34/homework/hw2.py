def find_max_element():
    numbers = [3, 7, 2, 15, 9, 1]
    max_number = numbers[0]

    for num in numbers:
        if num > max_number:
            max_number = num

    print("სიის უდიდესი ელემენტია:", max_number)

find_max_element()