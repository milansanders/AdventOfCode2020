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


tiles = set()
for line in open('input.txt', 'r').readlines():
    print()
    line = line.rstrip()
    instructions = []
    while len(line) > 0:
        if line[0] == "s" or line[0] == "n":
            instructions.append(line[0:2])
            line = line[2:]
        else:
            instructions.append(line[0])
            line = line[1:]
    print("instructions: " + str(instructions))
    steps = list(map(map_instruction, instructions))
    print("steps: " + str(steps))
    tile = reduce(lambda coord1, coord2: ((coord1[0] + coord2[0]), (coord1[1] + coord2[1])), steps)
    print("tile: " + str(tile))
    if tile in tiles:
        tiles.remove(tile)
    else:
        tiles.add(tile)
print("\ntiles: " + str(tiles))
print("Black tiles: " + str(len(tiles)))
