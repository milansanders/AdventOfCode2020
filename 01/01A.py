lines = list(map(int, open('input.txt', 'r').readlines()))
for i in lines:
    for j in lines:
        if (i+j) == 2020:
            print("%d * %d = %d" % (i, j, i*j))
