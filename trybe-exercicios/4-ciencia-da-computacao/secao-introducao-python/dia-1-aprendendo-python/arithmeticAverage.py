def arithmeticAverage(list):
    sum = 0
    for value in list:
        sum += value
    result = sum / len(list)
    return print(result)


arithmeticAverage([2, 4, 6, 8])
