nb_moves = 10000000
nb_cups = 1000000
# cups = list(map(int, list("389125467"))) # Test
cups = list(map(int, list("583976241"))) # Input
cups += list(range(max(cups) + 1, nb_cups+1))


def next_lowest(target, taken):
    min_cups = 1
    while min_cups in taken:
        min_cups += 1
    while target in taken:
        target -= 1
    if target < min_cups:
        return get_max_cups(taken, target)
    return target


def get_max_cups(taken, target):
    max_cups = nb_cups
    while max_cups == target or max_cups in taken:
        max_cups -= 1
    return max_cups


def find_loop(cups):
    states = dict()
    move = 1
    while move <= nb_moves:
        state_hash = hash(",".join(map(str, cups)))
        print("move %d state hash %d" % (move, state_hash))
        if state_hash in states:
            return states[state_hash], move, cups
        states[state_hash] = move
        destination = next_lowest(cups[0] - 1, set(cups[1:4]))
        target_idx = cups.index(destination)
        cups = cups[4:target_idx + 1] + cups[1:4] + cups[target_idx + 1:] + [cups[0]]
        move += 1
    return 0, move, cups


(loop_start, loop_end, final_cups) = find_loop(cups)
print("Found loop between moves %d and %d (%d moves long)" % (loop_start, loop_end, loop_end-loop_start))
f = open("cups.txt", "w+")
f.write("Loop start: %s\n" % str(loop_start))
f.write("Loop end: %s\n" % str(loop_end))
f.write("Cups:\n")
for cup in cups:
    f.write(str(cup) + "\n")
