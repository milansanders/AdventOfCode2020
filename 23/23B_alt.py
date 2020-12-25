import time
import datetime

nb_moves = 10000000
nb_cups = 1000000
# cups = list(map(int, list("389125467"))) # Test
cups = list(map(int, list("583976241"))) # Input
cups += list(range(max(cups) + 1, nb_cups+1))


class Link:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lookup = dict()

    def add(self, data):
        if self.head is None:
            link = Link(data, None)
            self.head = link
            self.head.next = self.head
            self.tail = self.head
        else:
            link = Link(data, self.head)
            self.tail.next = link
            self.tail = self.tail.next
        self.lookup[data] = link

    def shift(self):
        self.head = self.head.next

    def extract_taken(self):
        res = set()
        curr = self.head
        for _ in range(3):
            curr = curr.next
            res.add(curr.data)
        return res

    def make_move(self, data):
        head = self.head
        taken_begin = head.next
        taken_end = taken_begin.next.next
        cont = taken_end.next
        curr = self.lookup[data]
        head.next = cont
        taken_end.next = curr.next
        curr.next = taken_begin
        self.head = cont

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
    print("Last 100000 moves: %.3fs" % (float(diff) / 1000))
    print("Estimated end: " + format_time(start_millis + duration_est))


ll_cups = CircularLinkedList()
for cup in cups:
    ll_cups.add(cup)
cups = ll_cups
start_millis = int(round(time.time() * 1000))
prev_millis = start_millis
move = 1
while move <= nb_moves:
    if (move % 100000) == 0:
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
# print("cups: " + str(cups))
print("%d * %d = %d" % (cups.head.next.data, cups.head.next.next.data, cups.head.next.data * cups.head.next.next.data))
