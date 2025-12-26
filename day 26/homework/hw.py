# შექმენი ცარიელი სია
# მომხმარებელი შეიყვანს რიცხვებს მანამ, სანამ არ დაწერს "stop"
# დაამატე მხოლოდ დადებითი რიცხვები
# ბოლოს დაბეჭდე სია

nums = []

while True:
    user_input = input("შეიყვანე რიცხვი ან 'stop': ")
    if user_input == "stop":
        break
    num = int(user_input)
    if num > 0:
        nums.append(num)
print(nums)