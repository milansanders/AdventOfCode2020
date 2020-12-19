import re

inp = open('input_2.txt', 'r').read().split("\n\n")
rules = {}
for line in inp[0].split("\n"):
    line = line.split(": ")
    rules[int(line[0])] = line[1]


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


def get_valid_msgs(idx):
    if idx not in rules:
        return []
    rule = rules[idx]
    res = set()
    for perm in rule.split(" | "):
        if rule.startswith("\""):
            res.add(perm.split("\"")[1])
        else:
            valids = []
            for i in perm.split(" "):
                valids.append(get_valid_msgs(int(i)))
            appends = get_all_appends(valids)
            for elem in appends:
                res.add(elem)
    return res


msgs = inp[1].split("\n")
msgs_31 = get_valid_msgs(31)
msgs_42 = get_valid_msgs(42)
unit_len = len(list(msgs_42)[0])

# We know that rule 0 is "8 11", in both test and actual input
# So we need to find msgs that start with a random amount of msgs_42 and end with a smaller number of msgs_32
# msg must start with n>1 msg_42 groups followed by at least one and at most n-1 msg_31 groups

valid_msgs = set()
start_pat = re.compile("^(%s){2,}" % ("|".join(msgs_42)))
for msg in msgs:
    if (m_42 := re.search(start_pat, msg)) is not None:
        match_42 = m_42.group(0)
        match_42_length = len(match_42)
        nb_42_matches = int(match_42_length / unit_len)
        end_pat = re.compile("^(%s){1,%d}$" % ("|".join(msgs_31), nb_42_matches-1))
        if (m_31 := re.search(end_pat, msg[match_42_length:])) is not None:
            match_31 = m_31.group(0)
            match_31_length = len(match_31)
            nb_31_matches = int(match_31_length / unit_len)
            assert nb_42_matches > nb_31_matches
            assert (match_42 + match_31) == msg
            valid_msgs.add(msg)
print("Matched %d out of %d" % (len(valid_msgs), len(msgs)))
