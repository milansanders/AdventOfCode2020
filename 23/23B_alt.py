import time
import datetime

nb_moves = 1000000
nb_cups = 1000000
cups = list(map(int, list("389125467"))) # Test
# cups = list(map(int, list("583976241"))) # Input
cups += list(range(max(cups) + 1, nb_cups+1))


class Link:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        if self.head is None:
            self.head = Link(data, None)
            self.head.next = self.head
            self.tail = self.head
        else:
            self.tail.next = Link(data, self.head)
            self.tail = self.tail.next

    def shift(self):
        self.head = self.head.next

    def extract_taken(self):
        return [
            self.head.next.data,
            self.head.next.next.data,
            self.head.next.next.next.data,
        ]

    def make_move(self, data):
        head = self.head
        taken_begin = head.next
        taken_end = head.next.next.next
        curr = taken_end.next
        while curr.data != data:
            curr = curr.next
        head.next = taken_end.next
        taken_end.next = curr.next
        curr.next = taken_begin
        self.head = self.head.next

    def __str__(self):
        current = self.head
        res = []
        while current.next != self.head:
            res.append(current.data)
            current = current.next
        res.append(current.data)
        return ", ".join(map(str, res))


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


ll_cups = CircularLinkedList()
for cup in cups:
    ll_cups.add(cup)
cups = ll_cups
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
    # print("cups: " + str(cups))
    taken = cups.extract_taken()
    # print("pick up: " + ", ".join(map(str, taken)))
    destination = next_lowest(cups.head.data - 1, taken)
    # print("destination: " + str(destination))
    cups.make_move(destination)
    move += 1

print("\nFinal result:")
while cups.head.data != 1:
    cups.shift()
print("cups: " + str(cups))
print("%d * %d = %d" % (cups.head.next.data, cups.head.next.next.data, cups.head.next.data * cups.head.next.next.data))
