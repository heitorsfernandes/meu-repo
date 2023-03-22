def print_name(name):
    removed = 0
    while removed < len(name):
        for index in range(len(name) - removed):
            print(name[index], end='')
        print()
        removed += 1


print_name('Isadora')
