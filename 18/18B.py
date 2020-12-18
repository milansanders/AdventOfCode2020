import re

sum_pattern = re.compile('([0-9]+\+[0-9]+)')
mul_pattern = re.compile('([0-9]+\*[0-9]+)')

def pop_elem(line) -> (str, str):
    if len(line) == 0:
        return None, ""
    first = line[0]
    if first == "+" or first == "*" or first == "(" or first == ")":
        return first, line[1:]
    else:
        for i in range(len(line)):
            if not line[i].isdigit():
                return int(line[:i]), line[i:]
        return int(line), ""


def calc_op(a, op, b):
    if op is None:
        res = b
    elif op == "+":
        res = a + b
    elif op == "*":
        res = a * b
    else:
        raise
    # print("making calc: %s %s %d = %d" % (str(a), op, b, res))
    return res


def calc(line):
    # print("CALCULATING: " + line)
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
    # print("after parentheses: " + line)
    while "+" in line:
        m = re.search(sum_pattern, line)
        # print("found +: " + m.group(0))
        args = m.group(0).split("+")
        res = str(int(args[0]) + int(args[1]))
        start = m.start(0)
        end = m.end(0)
        before = line[:start]
        after = line[end:]
        # print("%s %s %s" % (before, res, after))
        line = before + res + after
    # print("after +: " + line)
    while "*" in line:
        m = re.search(mul_pattern, line)
        # print("found *: " + m.group(0))
        args = m.group(0).split("*")
        res = str(int(args[0]) * int(args[1]))
        start = m.start(0)
        end = m.end(0)
        before = line[:start]
        after = line[end:]
        # print("%s %s %s" % (before, res, after))
        line = before + res + after
    # print("result: " + line)
    return int(line)


acc = 0
for line in map(lambda l: l.rstrip().replace(" ", ""), open("input.txt", "r").readlines()):
    res = calc(line)
    print("%s = %d" % (line, res))
    acc += res
print("Sum of all results: " + str(acc))
