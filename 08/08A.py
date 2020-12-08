program = list(map(lambda line: line.rstrip(), open('input.txt', 'r').readlines()[:-1]))
acc = 0
ctr = 0
executed_lines = set()

while ctr not in executed_lines:
    executed_lines.add(ctr)
    line = program[ctr]
    op = line.split(" ")[0]
    arg = int(line.split(" ")[1])
    if op == "nop":
        ctr += 1
    elif op == "acc":
        acc += arg
        ctr += 1
    else:
        ctr += arg

print("Accumulator: " + str(acc))
