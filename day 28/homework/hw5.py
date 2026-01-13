# მომხმარებელს შეაყვანინე რიცხვები, მანამ სანამ არ შეიყვანს 0, ყოველი რიცხვის შემდეგ დაბეჭდე "დადებითია" ან "უარყოფითია".დაბეჭდე ბოლოს რიცხვების ჯამი. გამოიყენე while loop.


total = 0

while True:
    number = int(input("შეიყვანე რიცხვი : "))
    if number == 0:
        break
    elif number > 0:
        print("დადებითია")
    else:
        print("უარყოფითია")
    total = total + number
print(total)