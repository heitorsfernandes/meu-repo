def biggestName(names):
    biggest = ''
    for name in names:
        if len(biggest) < len(name):
            biggest = name
    return print(biggest)


biggestName(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"])
