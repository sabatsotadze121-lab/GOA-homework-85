# 10) დაწერეთ ფუქნცია, რომელიც პარამეტრად მიიღებს იმ რაოდენობას, რამდენჯერად უნდა გამოკონსოლდეს "Hello, World".


def print_hello(times):
    for _ in range(times):
        print("Hello, World")

print_hello(3)