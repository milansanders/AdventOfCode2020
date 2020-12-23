import time
import datetime

nb_moves = 1000000
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


def format_time(m):
    return datetime.datetime.fromtimestamp(float(m) / 1000).strftime('%Y-%m-%d %H:%M')


def print_estimate(start_millis, millis, diff, duration_est):
    print("Started on: " + format_time(start_millis))
    print("Been going for: %.3fs" % (float(millis - start_millis) / 1000))
    print("Last 100 moves: %.3fs" % (float(diff) / 1000))
    print("Estimated end: " + format_time(start_millis + duration_est))


start_millis = int(round(time.time() * 1000))
prev_millis = start_millis
move = 1
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
    # print("\n-- move %d --" % move)
    # print("cups: (%d) %s" % (cups[0], " ".join(map(str, cups[1:]))))
    # print("pick up: %s" % ",".join(map(str, cups[1:4])))
    destination = next_lowest(cups[0] - 1, set(cups[1:4]))
    target_idx = cups.index(destination)
    cups[4:(target_idx+1)], cups[1:4] = cups[1:4], cups[4:(target_idx+1)]
    cups = cups[1:] + [cups[0]]
    move += 1

print("\nFinal result:")
print("cups: (%d) %s" % (cups[0], " ".join(map(str, cups[1:]))))

idx_1 = cups.index(1)
result = cups[idx_1+1:] + cups[:idx_1]
print("\nResult: " + "".join(map(str, result)))
result = (result[1], result[2])
print("%d * %d = %d" % (result[0], result[1], result[0]*result[1]))
