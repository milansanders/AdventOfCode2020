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
    # print("CALCULATING " + line)
    res = None
    next_op = None
    while len(line) > 0:
        (elem, line) = pop_elem(line)
        # print("res: %s; next_op: %s, line:%s %s" % (str(res), next_op, elem, line))
        if elem == "(":
            # print("jumping into parentheses")
            (inter_res, line) = calc(line)
            res, next_op = (calc_op(res, next_op, inter_res), None)
        elif elem == ")":
            break
        elif elem == "+" or elem == "*":
            # print("setting op to: " + elem)
            next_op = elem
        elif res is None:
            # print("Setting res to " + str(elem))
            res = elem
        else:
            res, next_op = (calc_op(res, next_op, elem), None)
    # print("RETURNING %d WITH REST OF LINE: %s" % (res, line))
    return (res, line)


acc = 0
for line in map(lambda l: l.rstrip().replace(" ", ""), open("input.txt", "r").readlines()):
    res, _ = calc(line)
    print("%s = %d" % (line, res))
    acc += res
print("Sum of all results: " + str(acc))
