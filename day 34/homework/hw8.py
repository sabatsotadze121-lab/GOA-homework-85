def sum_of_digits():
    text = input("შეიყვანეთ ტექსტი (ასოები და ციფრები): ")
    total = 0

    for char in text:
        if char.isdigit():
            total += int(char)

    print("ტექსტში არსებული ციფრების ჯამია:", total)

sum_of_digits()