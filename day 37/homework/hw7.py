def number_type():
    num = int(input("შეიყვანე რიცხვი: "))
    if num > 0:
        return "დადებითია"
    elif num < 0:
        return "უარყოფითია"
    else:
        return "ნულია"

print(number_type())