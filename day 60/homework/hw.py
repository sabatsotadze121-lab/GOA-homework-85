def is_valid_walk(walk):
    ns = 0
    ew = 0
    if len(walk) == 10:
        for step in walk:
            if step == 'n':
                ns += 1
            if step == 's':
                ns -= 1
            if step == 'w':
                ew += 1               
            if step == 'e':
                ew -= 1            
    else:
        return False
    return ns == 0 and ew == 0