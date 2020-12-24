from functools import reduce


def map_instruction(instruction):
    if instruction == "e":
        return 1, 0
    elif instruction == "w":
        return -1, 0
    elif instruction == "ne":
        return 0, 1
    elif instruction == "nw":
        return -1, 1
    elif instruction == "se":
        return 1, -1
    elif instruction == "sw":
        return 0, -1


def get_neighbours(x, y):
    neighbours = [(1, 0), (-1, 0), (0, 1), (-1, 1), (1, -1), (0, -1)]
    neighbours = list(map(lambda n: (n[0] + x, n[1] + y), neighbours))
    return neighbours


def flip_tiles(tiles):
    new_tiles = set()
    xs = list(map(lambda c: c[0], tiles))
    ys = list(map(lambda c: c[1], tiles))
    for x in range(min(xs) - 1, max(xs) + 2):
        for y in range(min(ys) - 1, max(ys) + 2):
            tile = (x, y)
            nb_neigbours = len(list(filter(lambda t: t in tiles, get_neighbours(x, y))))
            if tile in tiles:
                if 0 < nb_neigbours <= 2:
                    new_tiles.add(tile)
            elif nb_neigbours == 2:
                new_tiles.add(tile)
    return new_tiles


tiles = set()
for line in open('input.txt', 'r').readlines():
    line = line.rstrip()
    instructions = []
    while len(line) > 0:
        if line[0] == "s" or line[0] == "n":
            instructions.append(line[0:2])
            line = line[2:]
        else:
            instructions.append(line[0])
            line = line[1:]
    steps = list(map(map_instruction, instructions))
    tile = reduce(lambda coord1, coord2: ((coord1[0] + coord2[0]), (coord1[1] + coord2[1])), steps)
    if tile in tiles:
        tiles.remove(tile)
    else:
        tiles.add(tile)

day = 0
while day <= 100:
    print("Day %d: %d" % (day, len(tiles)))
    tiles = flip_tiles(tiles)
    day += 1
