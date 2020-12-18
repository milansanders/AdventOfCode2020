import re

par_pattern = re.compile('\\(([^()]+)\\)')
sum_pattern = re.compile('([0-9]+)\\+([0-9]+)')
mul_pattern = re.compile('([0-9]+)\\*([0-9]+)')


def calc(line):
    while (m := re.search(par_pattern, line)) is not None:
        line = line[:m.start(0)] + str(calc(m.group(1))) + line[m.end(0):]
    while (m := re.search(sum_pattern, line)) is not None:
        line = line[:m.start(0)] + str(int(m.group(1)) + int(m.group(2))) + line[m.end(0):]
    while (m := re.search(mul_pattern, line)) is not None:
        line = line[:m.start(0)] + str(int(m.group(1)) * int(m.group(2))) + line[m.end(0):]
    return int(line)


acc = 0
for line in map(lambda l: l.rstrip().replace(" ", ""), open("input.txt", "r").readlines()):
    res = calc(line)
    print("%s = %d" % (line, res))
    acc += res
print("Sum of all results: " + str(acc))
