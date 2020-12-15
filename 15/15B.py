import time

t_0 = 30000000


def play_game(preamble):
    memory = {preamble[i]: i for i in range(len(preamble) - 1)}
    t = len(preamble) - 1
    last = preamble[t]
    while t < t_0 - 1:
        if last in memory:
            new = t - memory[last]
        else:
            new = 0
        memory[last] = t
        last = new
        t += 1
    return last


actual_preamble = list(map(int, open('input.txt', 'r').readlines()[0].split(",")))
start = time.time()
res = play_game(actual_preamble)
end = time.time()
print("%s: number %d is %d after %ds" % (actual_preamble, t_0, res, end - start))
