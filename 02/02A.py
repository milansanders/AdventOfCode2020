from functools import reduce

nbValids = 0
for line in open('input.txt', 'r').readlines():
    (range, letter, pw) = line.split(" ")
    (rangeMin, rangeMax) = list(map(int, range.split("-")))
    letter = letter[0]

    count = reduce(lambda count, l: count + 1 if l == letter else count, pw, 0)
    if rangeMin <= count <= rangeMax:
        nbValids += 1
print(nbValids)
