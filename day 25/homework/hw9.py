#  შექმენი list: nums = [1, 2, 3, 4] მომხმარებელს შეაყვანინე: ინდექსი და რიცხვი, თუ ინდექსი list-ის საზღვრებშია გამოიყენე insert() ჩასამატებლად, თუ ინდექსი ლისტზე დიდია მაშინ გამოიყენე append()


nums = [1, 2, 3, 4]

aaa = int(input("შეიყვანე ინდექსი: "))
num = int(input("შეიყვანე რიცხვი: "))

if aaa < len(nums):
    nums.insert(aaa, num)
else:
    nums.append(num)

print(nums)