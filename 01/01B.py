lines = list(map(int, open('input.txt', 'r').readlines()))
for i in lines:
    for j in lines:
        for k in lines:
            if (i+j+k) == 2020:
                print("%d * %d * %d = %d" % (i, j, k, i*j*k))
