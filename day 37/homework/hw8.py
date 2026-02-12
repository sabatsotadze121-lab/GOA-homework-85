# 8) შექმენი ფუქნცია რომელიც მიიღებს რაღაც ტექსტს და ასევე რაღაც რიცხვს, ტექსტსში ყველა ასოა აქციე დიდად და რიცხვითი მნიშვნელობა გადააქცია სტრინგის ტიპად.

def text_and_number(text, number):
    return text.upper(), str(number)

print(text_and_number("hello", 123))