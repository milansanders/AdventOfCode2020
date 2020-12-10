from functools import reduce

adapters: [int] = list(map(lambda line: int(line.rstrip()), open('input.txt', 'r').readlines()))
jolts = [0] + sorted(adapters) + [max(adapters) + 3]
print("list of jolts: " + str(jolts))
differences: [int] = [jolts[i + 1] - jolts[i] for i in range(len(jolts) - 1)]
print("list of differences: " + str(differences))

runs_of_one: [int] = list(filter(lambda run: run > 1, map(len, "".join(map(str, differences)).split("3"))))
print("Length of consecutive runs of 1 jolts differences: " + str(runs_of_one))


# Combinatorics isn't my strong suite
def permutations(run: int) -> int:
    if run == 2:
        return 2
    if run == 3:
        return 4
    if run == 4:
        return 7
    else:
        return 1


perms: [int] = map(permutations, runs_of_one)
print(reduce(lambda a, b: a*b, perms))
