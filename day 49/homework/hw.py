def reverse_words(text):
    arr = text.split(" ")
    rslt_arr = []

    for word in arr:
            rslt_arr.append(word[::-1])

    rslt = ""
    for word1 in rslt_arr:
        rslt += word1
        rslt += " "

    return rslt[:len(rslt)-1]