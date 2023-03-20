def biggest_name(names):
    biggest = ''
    for name in names:
        if len(biggest) < len(name):
            biggest = name
    return print(biggest)


biggest_name(["José", "Lucas", "Nádia", "Fernanda", "Cairo", "Joana"])
