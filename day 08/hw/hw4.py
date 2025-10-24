#მომხმარებელს შემოატანინე:
#--> ასაკი (age)
#--> სტუდენტია თუ არა (student) – შეიყვანოს "yes" ან "no"
#შემდეგ:
#თუ ასაკი ნაკლებია 12-ზე ან მეტია 65-ზე -> "ბილეთი უფასოა"
#თუ student == "yes" და ასაკი მეტია 12-ზე -> "ბილეთი ნახევარ ფასად"
#სხვა შემთხვევაში -> "სრული ფასი უნდა გადაიხადო"


age = int(input("Enter your age: "))
student = input("Are you a student? ")


if age < 12 or age > 65:
    print("The ticket is free")
elif student == "yes" and age >= 12:
    print("The ticket is half price")
else:
    print("You have to pay full price")
