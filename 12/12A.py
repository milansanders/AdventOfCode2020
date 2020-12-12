import math

instructions = list(map(lambda line: line.rstrip(), open('input.txt', 'r').readlines()))
print(instructions)
x = 0
y = 0
a = 0

for instruction in instructions:
    print("")
    op = instruction[0]
    val = int(instruction[1:])
    print((op, val))
    if op == "N":
        y += val
    elif op == "S":
        y -= val
    elif op == "E":
        x += val
    elif op == "W":
        x -= val
    elif op == "L":
        a = (a+val) % 360
    elif op == "R":
        a = (a-val) % 360
    elif op == "F":
        rad = math.radians(a)
        dx = int(math.cos(rad) * val)
        dy = int(math.sin(rad) * val)
        x += dx
        y += dy
    else:
        print("OP UNKNOWN: " + instruction)
    print("(%d,%d)@%d°" % (x, y, a))

print("\n(%d,%d)@%d°: %d" % (x, y, a, abs(x)+abs(y)))
