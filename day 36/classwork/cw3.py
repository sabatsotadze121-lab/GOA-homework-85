# 3) შექმენით ფუნცქცია სახელად sum_numbers რომელიც პარამეტრად მიიღებს რიცხვების სიას [10, 20,30, 100, 200, 500 ] დაწერე ფუნქცია რომელიც დააბრუნებს მოცემული რიცხვების ჯამს

def sum_numbers(numbers):
    total = 0
    for num in numbers:
        total = total + num
    return total


nums = [10, 20, 30, 100, 200, 500]
aaa = sum_numbers(nums)
print(aaa)