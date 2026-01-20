# 1)შექმენი სია სადაც მოათავსებთ განსხვავებული ტიპის მონაცემებს,შენი დავალებაა რომ გაიგო თუ რამდენი ცალი სტრინგ ტიპის მონაცემი გვხვდება სიაში

list = [10, "hello", 3.14, "world", True, "Python"]

strings = 0

for i in range(len(list)):
    if type(list[i]) == str:
        strings = strings + 1

print("სტრინგების რაოდენობა:", strings)