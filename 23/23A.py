cups = list(map(int, list("583976241")))


def next_lowest(target, cups):
    if target < min(cups):
        return max(cups)
    while target not in cups:
        target -= 1
    return target


round = 1
while round <= 100:
    print("\n-- move %d --" % round)
    print("cups: (%d) %s" % (cups[0], " ".join(map(str, cups[1:]))))
    print("pick up: %s" % ",".join(map(str, cups[1:4])))
    target_idx = cups.index(next_lowest(cups[0] - 1, cups[4:]))
    cups = cups[4:(target_idx+1)] + cups[1:4] + cups[target_idx+1:] + [cups[0]]
    round += 1

idx_1 = cups.index(1)
result = cups[idx_1+1:] + cups[:idx_1]
print("\nResult: " + "".join(map(str, result)))