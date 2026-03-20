def two_oldest_ages(ages):
    b = 0
    a = 0
    for i in ages:
        if b < i:
            b = i
    
    c = ages.remove(b)
    for j in ages:
        if a < j:
            a = j        
    return([a,b])