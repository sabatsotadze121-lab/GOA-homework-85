# შექმენი ცარიელი list, მომხმარებელს 5-ჯერ შეაყვანინე რიცხვი, ყველა დაამატე list-ში და საბოლოოდ for loop-ის გამოყენებით დააჯამე რიცხვები რომელიც გექნება ლისტში

nums = []
total = 0

for i in range(5):
    num = int(input("შეიყვანე რიცხვი: "))
    nums.append(num)

for i in nums:
    total = total + i

print("ჯამი:" , total)