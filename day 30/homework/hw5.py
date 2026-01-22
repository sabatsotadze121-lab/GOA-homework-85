# 5) შექმენით სტრინგის ცვლადი და ცარიელი სია, თუ სტრინგის ასო არის პატარა, მაშინ ცარიელ სიაში ჩაამატეთ "%" ნიშანი, ხოლო თუ სტრინგის ასო არის დიდი, მაშინ ცარიელ სიაში ჩაამატეთ "@" ნიშანი. თუ მინუსების რაოდენობა სიაში არის ლუწი, მაშინ წაშალე ყველა "%" ნიშანი, ხოლო თუ მინუსების რაოდენობა სიაში არის კენტი, წაშალე ყველა "@" ნიშანი. "%" და "@" -ების თავიდან სიაში ჩასაგდებად გამოიყენეთ for ციკლი, ხოლო "%" ან "@" -ების წასაშლელად გამოიყენეთ while ციკლი.

text = "Hello World"
symbols = []


for char in text:
    if char.islower():
        symbols.append("%")
    elif char.isupper():
        symbols.append("@")


count_at = symbols.count("@")

i = 0
while i < len(symbols):
    if count_at % 2 == 0: 
        if symbols[i] == "%":
            symbols.remove(symbols[i])
            
    else: 
        if symbols[i] == "@":
            symbols.remove(symbols[i])
            
    i = i + 1

print(symbols)