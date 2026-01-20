# 5)შექმენი სია სადაც შეიყვანთ როგორდც დადებით ასევე უარყოფით რიცხვებს,შენი დავალებაა გაიგო სიაშ მყოფი დადებით რიცხვების ჯამი და უარყოფით რიცხვების რაოდენობა

list = [-1 , 5, 10, -20 , 200, 100 , -40]
dadebiti = 0
uaryofiti = 0

for i in range(len(list)):
    if list[i] > 0 :
        dadebiti = dadebiti + 1
    elif list[i] < 0 :
        uaryofiti = uaryofiti + 1

print(dadebiti)
print(uaryofiti)

