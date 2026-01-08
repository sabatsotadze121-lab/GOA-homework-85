# მომხმარებელი შეიყვანს რიცხვებს
# დადებითი რიცხვები დაამატე დადებითების სიაში
# უარყოფითი რიცხვები დაამატე უარყოფითების სიაში
# ბოლოს დაბეჭდე ორივე სია

positive = []
negative = []

count = int(input("რამდენი რიცხვი გინდა?: "))
for i in range(count):
    num = int(input("შეიყვანე რიცხვი: "))
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print("დადებითი - " , positive)
print("უარყოფითი - " , negative)