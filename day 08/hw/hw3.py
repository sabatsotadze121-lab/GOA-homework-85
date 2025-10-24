#მომხმარებელს შემოატანინე:
#--> ტემპერატურა (temp)
#--> არის თუ არა წვიმა (rain) – მომხმარებელმა შეიყვანოს "yes" ან "no"
#შემდეგ შეამოწმე:
#თუ ტემპერატურა მეტია 25-ზე და rain == "no" -> "შესანიშნავი ამინდია სასეირნოდ!"
#თუ ტემპერატურა მეტია 25-ზე და rain == "yes" -> "ცხელი და წვიმიანია, ჩაფხუტი დაგჭირდება!"
#თუ ტემპერატურა ნაკლებია 10-ზე ან rain == "yes" -> "სჯობს სახლში დარჩე"
#სხვა შემთხვევაში -> "სასიამოვნო ამინდია"



temp = int(input("Enter temperature : "))
rain = input("Is it raining?: ")

if temp > 25 and rain == "no":
    print("It's a great day for a walk")
elif temp > 25 and rain == "yes":
    print("It's hot and rainy, you hat")
elif temp < 10 or rain == "yes":
    print("Better to stay home")
else:
    print("It's a pleasant weather")

    
