nbValids = 0
for line in open('input.txt', 'r').readlines():
    (range, letter, pw) = line.split(" ")
    (rangeMin, rangeMax) = list(map(int, range.split("-")))
    letter = letter[0]

    if (pw[rangeMin-1] == letter) != (pw[rangeMax-1] == letter):
        nbValids += 1
print(nbValids)
