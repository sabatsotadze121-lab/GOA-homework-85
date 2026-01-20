# 1)შექმენი სია სადაც მოათავსებთ განსხვავებული ტიპის მონაცემებს,შენი დავალებაა რომ გაიგო თუ რამდენი ცალი სტრინგ ტიპის მონაცემი გვხვდება სიაში

list10, "hello", 3.14, "world", True, "Python"]

count_strings = 0

for i in range(len(data)):
    if type(data[i]) == str:
        count_strings += 1

print("სტრინგების რაოდენობა:", count_strings)