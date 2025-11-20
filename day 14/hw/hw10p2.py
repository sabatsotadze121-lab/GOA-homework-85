# მომხმარებელს შემოატანინეთ რიცხვი, ამ რიცხვის
#  ჩათვლით შეკრიბეთ ყველა რიცხვი და გამოიტანეთ საბოლოო პასუხი.

number = int(input("შეიყვანეთ  რიცხვი: "))

if number < 1:
    print("გაითვალისწინეთ: შეიყვანეთ 1 ან მეტი.")
else:
    total = 0
    for i in range(1, number + 1):
        total = total + i
    print(total)