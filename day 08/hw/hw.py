#მომხმარებელს შემოატანინე ტემპერატურა (რიცხვი) და შემდეგ შეამოწმე:
#თუ ტემპერატურა მეტია 30-ზე -> დაბეჭდე "ძალიან ცხელა!"
#თუ ტემპერატურა მეტია 20-ზე -> დაბეჭდე "სასიამოვნო ამინდია"
#თუ ტემპერატურა მეტია 10-ზე -> დაბეჭდე "ცოტა ცივა"
#თუ ტემპერატურა მეტია 0-ზე -> დაბეჭდე "ცივა, ჩაიცვი თბილად"
#სხვა შემთხვევაში -> "გაიყინები, სახლში დარჩი!"








temp = int(input("Enter temperature : "))

if temp > 30:
    print("its too hot")
elif temp > 20:
    print("its a pretty good temperature")
elif temp > 10:
    print("its getting little cold")
elif temp > 0:
    print("its cold, better wear a jacket")
else:
    print("stay home")

