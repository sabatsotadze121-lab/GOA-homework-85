# შექმენი list: letters = ["a", "b", "c", "d", "e"] მომხმარებელს შეაყვანინე ინდექსი, pop()-ით წაშალე ამ ინდექსზე მდგომი ელემენტი, დაბეჭდე წაშლილი ელემენტი და list

letters = ["a", "b", "c", "d", "e"]

aaa = int(input("შეიყვანე ინდექსი: "))
aa = letters.pop(aaa)

print("წაშლილი ელემენტი:" , aa)
print("list:" , letters)