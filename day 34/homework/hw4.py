def count_long_words_split():
    sentence = input("შეიყვანეთ წინადადება: ")
    words = sentence.split()
    count = 0

    for word in words:
        if len(word) > 4:
            count += 1

    print("4-ზე მეტი სიგრძის სიტყვების რაოდენობაა:", count)

count_long_words_split()