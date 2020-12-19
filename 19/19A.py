inp = open('input_1.txt', 'r').read().split("\n\n")
rules = {}
for line in inp[0].split("\n"):
    line = line.split(": ")
    rules[int(line[0])] = line[1]
# print(rules)


def get_all_appends(elems: [[str]]) -> [str]:
    # print("getting valid appends of: " + str(elems))
    res = []
    if len(elems) == 1:
        return elems[0]
    for head in elems[0]:
        tails = get_all_appends(elems[1:])
        # print("head %s has tails %s" % (head, tails))
        for tail in tails:
            # print("Found head and tail: %s & %s" % (head, tail))
            res.append(head + tail)
    # print("%s has valid appends: %s" % (str(elems), str(res)))
    return res


def get_valid_msgs(idx) -> [str]:
    rule = rules[idx]
    if rule.startswith("\""):
        return [rule[1]]
    res = []
    for perm in rule.split(" | "):
        # print("resolving: " + perm)
        valids = []
        for i in perm.split(" "):
            i = int(i)
            valid_msgs = get_valid_msgs(int(i))
            # print("valid msgs for %d: %s" % (i, valid_msgs))
            valids.append(valid_msgs)
        appends = get_all_appends(valids)
        # print("%s get_all_appends: %s" % (valids, appends))
        res += appends
    return res


valid_msgs = get_valid_msgs(0)
print("Valid messages: " + str(valid_msgs))
print("Matching messages: " + str(len(list(filter(lambda msg: msg in valid_msgs, inp[1].split("\n"))))))
