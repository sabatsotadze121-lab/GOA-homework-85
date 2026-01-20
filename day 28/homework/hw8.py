
# მომხმარებელს შეაყვანინე 5 რიცხვი while loopით, დაითვალე მათი საშუალო, თუ საშუალო > 50 დაბეჭდე "დიდი საშუალო" წინააღმდეგ შემთხვევაში "პატარა საშუალო"
total = 0
i = 0
while i < 5:
    num = int(input("შეიყვანე რიცხვი: "))
    total = total + num
    i = i + 1
average = total / i
print("საშუალო:", average)

if average > 50:
    print("დიდი საშუალო")
else:
    print("პატარა საშუალო")