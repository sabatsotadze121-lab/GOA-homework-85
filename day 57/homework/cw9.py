def nb_dig(n, d):
    s = 0
    for i in range(n+1):
        n = i ** 2
        if str(d) in str(n):
            s += str(n).count(str(d))
    return s