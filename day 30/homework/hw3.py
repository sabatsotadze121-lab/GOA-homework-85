# 3) შექმენით ქვეყნების სია, წაშალეთ pop() ან remove() ფუნქციით ყველა ის სიტყვა რომლის ყველა ასო არის დიდი, ხოლო ყველა სხვა სიტყვას ყველა ასო გაუხადეთ დიდი. დაპრინტეთ საბოლოო შედეგი. გამოიყენეთ while ციკლი.

countries = ["Georgia", "usa", "France", "uk", "germany"]
i = 0

while i < len(countries):
    if countries[i].isupper():
        countries.pop(i)
    else:
        countries[i] = countries[i].upper()
        i = i + 1

print(countries)