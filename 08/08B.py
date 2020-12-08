original_program = list(map(lambda line: line.rstrip(), open('input.txt', 'r').readlines()))


def alter_program(line_nr):
    program = original_program.copy()
    line = program[line_nr]
    op = line.split(" ")[0]
    arg = int(line.split(" ")[1])
    if op == "jmp":
        op = "nop"
    elif op == "nop":
        op = "jmp"
    program[line_nr] = op + " " + str(arg)
    return program


def run(altered_line):
    program = alter_program(altered_line)
    acc = 0
    ctr = 0
    executed_lines = set()
    finished_properly = True
    while ctr < len(program):
        line = program[ctr]
        op = line.split(" ")[0]
        arg = int(line.split(" ")[1])
        executed_lines.add(ctr)
        if op == "nop":
            ctr += 1
        elif op == "acc":
            acc += arg
            ctr += 1
        else:
            ctr += arg
        if ctr in executed_lines:
            finished_properly = False
            break
    return finished_properly, acc


for i in range(len(original_program)):
    (finished_properly, acc) = run(i)
    if finished_properly:
        print(acc)
        break
