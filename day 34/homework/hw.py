def aaaa():
    n = int(input("შეიყვანეთ მთელი რიცხვი: "))
    aa = 0

    for i in range(n):
        if i % 2 == 0:
            aa = aa + 1

    print("ლუწი რიცხვების რაოდენობა:", aa)

aaaa()