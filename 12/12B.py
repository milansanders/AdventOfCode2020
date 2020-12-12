instructions = list(map(lambda line: line.rstrip(), open('input.txt', 'r').readlines()))
print(instructions)
sx = 0
sy = 0
wx = 10
wy = 1


def turn_left(x, y):
    return -y, x


def turn_right(x, y):
    return y, -x


for instruction in instructions:
    print("")
    op = instruction[0]
    val = int(instruction[1:])
    print((op, val))
    if op == "N":
        wy += val
    elif op == "S":
        wy -= val
    elif op == "E":
        wx += val
    elif op == "W":
        wx -= val
    elif op == "L":
        if val == 90:
            (wx, wy) = turn_left(wx, wy)
        elif val == 180:
            (wx, wy) = (-wx, -wy)
        elif val == 270:
            (wx, wy) = turn_right(wx, wy)
    elif op == "R":
        if val == 90:
            (wx, wy) = turn_right(wx, wy)
        elif val == 180:
            (wx, wy) = (-wx, -wy)
        elif val == 270:
            (wx, wy) = turn_left(wx, wy)
    elif op == "F":
        sx += val*wx
        sy += val*wy
    else:
        print("OP UNKNOWN: " + instruction)
    print("ship:(%d,%d) wp:(%d,%d)" % (sx, sy, wx, wy))

print("\n(%d,%d): %d" % (sx, sy, abs(sx)+abs(sy)))
