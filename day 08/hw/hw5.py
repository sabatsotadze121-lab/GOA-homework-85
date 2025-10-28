#მომხმარებელს შემოატანინე:
#--> მომხმარებლის სახელი (username)
#--> პაროლი (password)
#შეამოწმე:
#თუ მომხმარებელი არის "admin" და პაროლი არის 'superSecretPassword' → "მოგესალმები, ადმინ!"
#თუ მომხმარებელი "guest" და პაროლი არის "1234" → "მოგესალმები, სტუმარო!"
#სხვა შემთხვევაში → "მომხმარებელი არ მოიძებნა!"



username = input("შეიყვანეთ მომხმარებლის სახელი: ")
password = int(input("შეიყვანეთ პაროლი: "))


if username == "admin" and password == "superSecretPassword":
    print("მოგესალმები, ადმინ!")
elif username == "guest" and password == "1234":
    print("მოგესალმები, სტუმარო!")
else:
    print("მომხმარებელი არ მოიძებნა!")

    