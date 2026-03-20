def xo(s):
    countX = 0
    countO = 0
    for i in s:
        if (i == 'X') | (i == 'x'):
            countX = countX + 1
        elif (i == 'O') | (i == 'o'):
            countO = countO + 1
    if countX == countO:     
        return True
    else:
        return False