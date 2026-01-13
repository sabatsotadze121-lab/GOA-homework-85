# მომხმარებელს შეაყვანინე ასაკი მანამ, სანამ არ შეიყვანს -1. დაბეჭდე რამდენი ადამიანი იყო არასრულწლოვანი, სრულწლოვანი, პენსიონერი. გამოიყენე while loop + if/elif/else

minor = 0
adult = 0
pensioner = 0

while True:
    age = int(input("შეიყვანე ასაკი : "))

    if age == -1:
        break
    elif age < 18:
        minor = minor + 1
    elif age < 65:
        adult = adult + 1
    else:
        pensioner = pensioner + 1

print("არასრულწლოვანი:" , minor)
print("სრულწლოვანი:" , adult)
print("პენსიონერი:" , pensioner)