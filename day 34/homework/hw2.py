# 2) შექმენით ფუნქცია. შექმენით რიცხვებით სავსე სია, დაბეჭდეთ სიის უდიდესი ელემენტი. არ გამოიყენოთ max() ფუნქცია, გამოიყენეთ for ციკლი. გამოიძახეთ ფუნქცია.

def find_max_element():
    numbers = [3, 5, 2, 15, 9, 1]
    max_number = 0

    for num in numbers:
        if num > max_number:
            max_number = num

    print("სიის უდიდესი ელემენტია:", max_number)

find_max_element()