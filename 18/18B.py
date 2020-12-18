import re

sum_pattern = re.compile('([0-9]+\+[0-9]+)')
mul_pattern = re.compile('([0-9]+\*[0-9]+)')

def calc(line):
    while "(" in line:
        depth = 0
        start = line.index("(")
        i = start+1
        while depth > 0 or line[i] != ")":
            if line[i] == "(":
                depth += 1
            if line[i] == ")":
                depth -= 1
            i += 1
        end = i
        line = line[:start] + str(calc(line[start+1:end])) + line[end+1:]
    while "+" in line:
        m = re.search(sum_pattern, line)
        args = m.group(0).split("+")
        line = line[:m.start(0)] + str(int(args[0]) + int(args[1])) + line[m.end(0):]
    while "*" in line:
        m = re.search(mul_pattern, line)
        args = m.group(0).split("*")
        line = line[:m.start(0)] + str(int(args[0]) * int(args[1])) + line[m.end(0):]
    return int(line)


acc = 0
for line in map(lambda l: l.rstrip().replace(" ", ""), open("input.txt", "r").readlines()):
    res = calc(line)
    print("%s = %d" % (line, res))
    acc += res
print("Sum of all results: " + str(acc))
