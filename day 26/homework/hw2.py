# შექმენი ცარიელი სია
# მომხმარებელი შეიყვანს რიცხვებს "stop"-მდე
# თუ რიცხვი ნაკლებია 50-ზე → ჩასვი დასაწყისში
# თუ მეტია ან ტოლია 50-ის → დაამატე ბოლოში
# ბოლოს დაბეჭდე სია

nums = []

while True:
    user_input = input("შეიყვანე რიცხვი ან 'stop': ")
    if user_input == "stop":
        break

    num = int(user_input)
    if num < 50:
        nums.insert(0, num)
    else:
        nums.append(num)

print(nums)