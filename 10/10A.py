adapters: [int] = [0] + sorted(list(map(lambda line: int(line.rstrip()), open('input.txt', 'r').readlines())))
print(adapters)
differences: [int] = [adapters[i+1] - adapters[i] for i in range(len(adapters)-1)] + [3]
print(differences)
nb_one = len(list(filter(lambda d: d == 1, differences)))
nb_three = len(list(filter(lambda d: d == 3, differences)))
print("%d * %d = %d" % (nb_one, nb_three, nb_one*nb_three))
