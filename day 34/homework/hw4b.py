def count_long_words_no_split():
    sentence = input("შეიყვანეთ წინადადება: ")
    count = 0
    length = 0

    for char in sentence:
        if char != " ":
            length += 1
        else:
            if length > 4:
                count += 1
            length = 0

    if length > 4:   
        count += 1

    print("4-ზე მეტი სიგრძის სიტყვების რაოდენობაა:", count)

count_long_words_no_split()