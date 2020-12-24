import time
import datetime
from collections import deque

nb_moves = 10000000
nb_cups = 1000000
cups = list(map(int, list("389125467"))) # Test
# cups = list(map(int, list("583976241"))) # Input
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


def format_time(m):
    return datetime.datetime.fromtimestamp(float(m) / 1000).strftime('%Y-%m-%d %H:%M')


def print_estimate(start_millis, millis, diff, duration_est):
    print("Started on: " + format_time(start_millis))
    print("Been going for: %.3fs" % (float(millis - start_millis) / 1000))
    print("Last 100 moves: %.3fs" % (float(diff) / 1000))
    print("Estimated end: " + format_time(start_millis + duration_est))


def inc(v, i=1):
    return (v + i) % nb_cups


def make_move(data, cups, pick_up, taken):
    ptrs = deque([pick_up[0], pick_up[1], pick_up[2], inc(pick_up[2])], maxlen=4)
    vals = deque([cups[ptrs[0]], cups[ptrs[1]], cups[ptrs[2]], cups[ptrs[3]]], maxlen=4)
    while vals[2] != data:
        cups[ptrs[0]] = vals[3]
        new_pts = inc(ptrs[3])
        ptrs.append(new_pts)
        vals.append(cups[new_pts])
    cups[ptrs[0]] = taken[0]
    cups[ptrs[1]] = taken[1]
    cups[ptrs[2]] = taken[2]


start_millis = int(round(time.time() * 1000))
prev_millis = start_millis
move = 1
curr = 0
while move <= nb_moves:
    if (move % 100) == 0:
        print("\n-- move %d --" % move)
        millis = int(round(time.time() * 1000))
        diff = millis - prev_millis
        dur_tot = millis - start_millis
        millis_per_move = dur_tot / move
        duration_est = millis_per_move * nb_moves
        print_estimate(start_millis, millis, diff, duration_est)
        prev_millis = millis
    print("\n-- move %d --" % move)
    # print("cups: %s(%d) %s" % (" ".join(map(str, cups[:curr])) + " " if curr > 0 else "", cups[curr], " ".join(map(str, cups[curr + 1:]))))
    pick_up = (inc(curr, 1), inc(curr, 2), inc(curr, 3))
    taken = (cups[pick_up[0]], cups[pick_up[1]], cups[pick_up[2]])
    # print("pick up: %s" % ",".join(map(str, taken)))
    destination = next_lowest(cups[curr] - 1, set(taken))
    # print("destination: " + str(destination))
    make_move(destination, cups, pick_up, taken)
    curr = pick_up[0]
    move += 1

print("\nFinal result:")
print("cups: (%d) %s" % (cups[0], " ".join(map(str, cups[1:]))))

idx_1 = cups.index(1)
result = cups[idx_1+1:] + cups[:idx_1]
print("\nResult: " + "".join(map(str, result)))
result = (result[1], result[2])
print("%d * %d = %d" % (result[0], result[1], result[0]*result[1]))
