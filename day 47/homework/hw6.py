def getCount(inputStr):
    num_vowels = 0
    for i in range (0, len(inputStr)):
        if (inputStr[i] == "a") or (inputStr[i] == "i") or (inputStr[i] == "u") or (inputStr[i] == "e") or (inputStr[i] == "o"):
            num_vowels = num_vowels + 1
    
    return num_vowels