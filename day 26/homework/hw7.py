# მომხმარებელი შეიყვანს რიცხვებს
# დაამატე რიცხვები სიაში
# თუ ორი მეზობელი ელემენტის ჯამი < 50 → წაშალე მეორე ელემენტი
# დაბეჭდე საბოლოო სია

nums = []

count = int(input("რამდენი რიცხვი გინდა?: "))
for i in range(count):
    nums.append(int(input("შეიყვანე რიცხვი: ")))

i = 0
while i < len(nums) - 1:
    if nums[i] + nums[i + 1] < 50:
        nums.pop(i + 1)
    else:
        i += 1

print(nums)