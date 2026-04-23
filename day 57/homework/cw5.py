def adjacent_element_product(array):
    res = array[0] * array[1]
    for x in range(len(array)-1):
        product = array[x] * array[x + 1]
        if product > res:
            res = product
    return res