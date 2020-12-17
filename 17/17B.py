import itertools

active_cubes = set()
inp = open('input.txt', 'r').readlines()
for y in range(len(inp)):
    line = list(inp[y])
    for x in range(len(inp[y])):
        if line[x] == "#":
            active_cubes.add((x, y, 0, 0))


def print_state(active_cubes):
    x_s = list(map(lambda cube: cube[0], active_cubes))
    y_s = list(map(lambda cube: cube[1], active_cubes))
    z_s = list(map(lambda cube: cube[2], active_cubes))
    w_s = list(map(lambda cube: cube[3], active_cubes))
    for w in range(min(w_s), max(w_s)+1):
        for z in range(min(z_s), max(z_s)+1):
            print("z=%d, w=%d" % (z, w))
            for y in range(min(y_s), max(y_s)+1):
                print("".join(["#" if (x,y,z,w) in active_cubes else "." for x in range(min(x_s), max(x_s)+1)]))
            print()


def active_neighbours(coord, state):
    (x, y, z, w) = coord
    combinations = list(itertools.product(list(range(-1, 2)), list(range(-1, 2)), list(range(-1, 2)), list(range(-1, 2))))
    combinations.remove((0, 0, 0, 0))
    targets = list(map(lambda t: (x + t[0], y + t[1], z + t[2], w + t[3]), combinations))
    neighbours = list(filter(lambda cube: cube in state, targets))
    return len(neighbours)


def remain_active(coord, state):
    return 2 <= active_neighbours(coord, state) <= 3


def remain_inactive(coord, state):
    return active_neighbours(coord, state) != 3


iter = 0
while iter < 6:
    print("ITERATION: " + str(iter))
    print_state(active_cubes)
    new_state = set()
    x_s = list(map(lambda cube: cube[0], active_cubes))
    y_s = list(map(lambda cube: cube[1], active_cubes))
    z_s = list(map(lambda cube: cube[2], active_cubes))
    w_s = list(map(lambda cube: cube[2], active_cubes))
    for w in range(min(w_s) - 1, max(w_s) + 2):
        for z in range(min(z_s) - 1, max(z_s) + 2):
            for y in range(min(y_s) - 1, max(y_s) + 2):
                for x in range(min(x_s) - 1, max(x_s) + 2):
                    coord = (x, y, z, w)
                    if coord in active_cubes and not remain_active(coord, active_cubes):
                        print(str(coord) + " becomes inactive")
                    elif coord not in active_cubes and not remain_inactive(coord, active_cubes):
                        print(str(coord) + " becomes active")
                        new_state.add(coord)
                    else:
                        print(str(coord) + " remains " + ("active" if coord in active_cubes else "inactive"))
                        if coord in active_cubes:
                            new_state.add(coord)
    active_cubes = new_state
    iter += 1

print_state(active_cubes)
print("Active cubes: " + str(len(active_cubes)))