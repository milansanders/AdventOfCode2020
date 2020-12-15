t_0 = 2020
test_cases = open('test.txt', 'r').readlines()
test_cases = map(lambda line: line.rstrip().split(":"), test_cases)
test_cases = [(int(k), list(map(int, v.split(',')))) for (k, v) in test_cases]
print(test_cases)


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


def play_test(params):
    (target, preamble) = params
    res = play_game(preamble)
    print("%s resulted in %d (target was %d): %s" % (preamble, res, target, 'SUCCESS' if res == target else 'FAIL'))


for target, preamble in test_cases:
    play_test((target, preamble))
actual_preamble = list(map(int, open('input.txt', 'r').readlines()[0].split(",")))
res = play_game(actual_preamble)
print()
print("Actual input:")
print("%s resulted in %d" % (actual_preamble, res))
