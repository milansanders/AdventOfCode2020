import math

instructions = list(map(lambda line: line.rstrip(), open('input.txt', 'r').readlines()))
print(instructions)
sx = 0
sy = 0
wx = 10
wy = 1

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
    elif op == "F":
        sx += val*wx
        sy += val*wy
    else:
        angle = val
        if op == "R":
            angle = -angle
        rad = math.atan2(wy, wx) + math.radians(angle)
        dist = math.dist((0, 0), (wx, wy))
        wx = int(round(math.cos(rad) * dist))
        wy = int(round(math.sin(rad) * dist))
    print("ship:(%d,%d) wp:(%d,%d)" % (sx, sy, wx, wy))

print("\n(%d,%d): %d" % (sx, sy, abs(sx)+abs(sy)))
