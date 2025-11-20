# მომხმარებელს შემოატანინეთ რიცხვი, ამ 
# რიცხვის ჩათვლით შეკრიბეთ ყველა რიცხვი და გამოიტანეთ საბოლოო პასუხი.



number = int(input("შეიყვანეთ რიცხვი: "))

if number < 1:
    print(" შეიყვანეთ 1 ან მეტი."); 
else:
    total = 0
    i = 1
    while i <= number:
        total = total + i
        i = i + 1
    print(total)






