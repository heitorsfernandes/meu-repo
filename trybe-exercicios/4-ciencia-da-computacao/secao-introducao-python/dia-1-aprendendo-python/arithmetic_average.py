def arithmetic_average(list):
    sum = 0
    for value in list:
        sum += value
    result = sum / len(list)
    return print(result)


arithmetic_average([2, 4, 6, 8])
