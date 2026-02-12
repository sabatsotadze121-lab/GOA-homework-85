# 12) დაწერეთ ფუნქცია სახელად sumDigits, რომელიც არგუმენტად იღებს რიცხვს და აბრუნებს მისი ციფრების ჯამს.


def sumDigits(number):
    total = 0
    for digit in str(abs(number)):
        total = total + int(digit)
    return total

print(sumDigits(1234))