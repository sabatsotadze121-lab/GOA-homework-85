# შექმენი list: animals = ["dog", "cat", "horse", "cow"] მომხმარებელს შეაყვანინე ცხოველის სახელი, თუ არსებობს  დაბეჭდე მისი index-იმ, თუ არა  "Animal not found"


animals = ["dog", "cat", "horse", "cow"]

animal = input("name any animal: ")

if animal in animals:
    print(animals.index(animal))
else:
    print("Animal not found")