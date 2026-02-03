def longest_word():
    sentence = input("შეიყვანეთ წინადადება: ")
    words = sentence.split()

    i = 0
    longest = words[0]

    while i < len(words):
        if len(words[i]) > len(longest):
            longest = words[i]
        i += 1

    print("ყველაზე გრძელი სიტყვაა:", longest)

longest_word()