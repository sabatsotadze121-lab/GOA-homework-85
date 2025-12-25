# 1) შექმენი list: names = ["nika", "luka", "giorgi"] მომხმარებელს შეაყვანინე: ინდექსი და სახელი, insert()-ის გამოყენებით ჩასვი სახელი მითითებულ ადგილას და დაბეჭდე შედეგი

names = ["nika", "luka", "giorgi"]

input1 = int(input("შეიყვანე ინდექსი: "))
name = input("შეიყვანე სახელი: ")

names.insert(input1 , name)
print(names)