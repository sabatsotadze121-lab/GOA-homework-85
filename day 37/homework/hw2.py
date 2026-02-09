def count(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char in vowels:
            count = count + 1
    return count

print(count("Education"))