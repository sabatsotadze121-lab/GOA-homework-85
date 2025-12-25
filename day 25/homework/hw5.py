# 5) შექმენი ნებისმიერი list 5 ელემენტით, მომხმარებელს ჰკითხე: გინდა list-ის გასუფთავება? (yes/no), თუ პასუხი "yes" გამოიყენე clear(), ბოლოს დაბეჭდე list

list = [1, 2, 3, 4, 5]

aaa = input("გინდა list-ის გასუფთავება? (yes/no): ")

if aaa == "yes":
    list.clear()

print(list)