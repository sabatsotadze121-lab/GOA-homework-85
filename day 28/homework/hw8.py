
# მომხმარებელს შეაყვანინე 5 რიცხვი while loopით, დაითვალე მათი საშუალო, თუ საშუალო > 50 დაბეჭდე "დიდი საშუალო" წინააღმდეგ შემთხვევაში "პატარა საშუალო"
total = 0
count = 0
while count < 5:
    num = int(input("შეიყვანე რიცხვი: "))
    total = total + num
    count = count + 1
average = total / count
print("საშუალო:", average)

if average > 50:
    print("დიდი საშუალო")
else:
    print("პატარა საშუალო")