# 4) შექმენით სტრინგის ცვლადი და ცარიელი სია. სტრინგში მყოფი დიდი ასოები გახადეთ პატარა და ამ სიაში ჩაამატეთ, ხოლო სტრინგში მყოფი პატარა ასოები გახადეთ დიდი და ასევე ჩააგდეთ ამ სიაში. დაპრინტეთ საბოლოო სია, გამოიყენეთ while ციკლი


text = "PiTonI maGariA"
new_list = []
i = 0

while i < len(text):
    aa = text[i]
    if aa.isupper():
        new_list.append(aa.lower())
    elif aa.islower():
        new_list.append(aa.upper())
    else:
        new_list.append(aa) 
    i = i + 1

print(new_list)