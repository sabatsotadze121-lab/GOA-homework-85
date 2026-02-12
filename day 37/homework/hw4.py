# 4) შექმენი ფუნქცია რომელიც მიიღებს სიტყვების სიას და დააბრუნებს მხოლოდ იმ სიტყვებს რომლებიც იწყება დიდი ასოთი


def capital_words(words):
    result = []
    for word in words:
        if word[0].isupper():
            result.append(word)
    return result

print(capital_words(["Apple", "banana", "Car", "dog"]))