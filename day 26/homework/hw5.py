# მომხმარებელი შეიყვანს რამდენიმე რიცხვს
# დაამატე რიცხვები სიაში
# გამოთვალე და დაბეჭდე საშუალო არითმეტიკული

nums = []

count = int(input("რამდენი რიცხვი გინდა?: "))
for i in range(count):
    nums.append(int(input("შეიყვანე რიცხვი: ")))

average = sum(nums) / len(nums)
print("საშუალო:", average)