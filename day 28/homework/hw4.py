# 4) მომხმარებელს შემოაყვანინე 5 რიცხვი, დაბეჭდე მათი ჯამი. გამოიყენე for loop და while loop.

# total = 0

# for i in range(5):
#     number = int(input("შეიყვანე რიცხვი: "))
#     total = total + number

# print(total)

total = 0
i = 0

while i < 5:
    number = int(input("შეიყვანე რიცხვი: "))
    total = total + number
    i = i + 1

print( total)