seats = list(map(lambda line: line.rstrip(), open('input.txt', 'r').readlines()))
h = len(seats)
w = len(seats[0])
changed = True


def print_seats(seats):
    for line in seats:
        print("".join(line))


def count_occupied(seats):
    return len(list(filter(lambda s: s == "#", seats)))


def count_total_occupied(seats):
    c = 0
    for line in seats:
        for seat in line:
            if seat == "#":
                c += 1
    return c


def get_adjacent(x, y, seats):
    targets = []
    if y > 0:
        targets.append((x, y - 1))
    if y < h - 1:
        targets.append((x, y + 1))
    if x > 0:
        targets.append((x - 1, y))
        if y > 0:
            targets.append((x - 1, y - 1))
        if y < h - 1:
            targets.append((x - 1, y + 1))
    if x < w - 1:
        targets.append((x + 1, y))
        if y > 0:
            targets.append((x + 1, y - 1))
        if y < h - 1:
            targets.append((x + 1, y + 1))
    return "".join(list(map(lambda coord: seats[coord[1]][coord[0]], targets)))


while changed:
    print_seats(seats)
    print("\n\n")
    changed = False
    new_seats = [["." for _ in range(w)] for _ in range(h)]
    for x in range(w):
        for y in range(h):
            seat = seats[y][x]
            if not seat == ".":
                adjacent = count_occupied(get_adjacent(x, y, seats))
                if seat == "L" and adjacent == 0:
                    new_seats[y][x] = "#"
                    changed = True
                elif seat == "#" and adjacent >= 4:
                    new_seats[y][x] = "L"
                    changed = True
                else:
                    new_seats[y][x] = seats[y][x]
    seats = [[new_seats[y][x] for x in range(w)] for y in range(h)]

print("Final config:\n")
print_seats(seats)
print("\n\n")
print("\nFinal occupied seats: " + str(count_total_occupied(seats)))
