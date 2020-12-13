inp = open('input.txt', 'r').readlines()
t_0 = int(inp[0])
lines = set(map(int, inp[1].replace("x,", "").replace(",x", "").split(",")))
print((t_0, lines))


def earliest_dep(t_0, lines):
    for t in range(t_0, t_0+min(lines)):
        for line in lines:
            if t % line == 0:
                return (t-t_0) * line


print(earliest_dep(t_0, lines))