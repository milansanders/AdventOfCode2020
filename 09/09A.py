import itertools

numbers: [int] = list(map(lambda line: int(line.rstrip()), open('input.txt', 'r').readlines()))
preamble_length: int = 25


def is_valid(preamble: [int], target: int) -> bool:
    return target in map(sum, itertools.combinations(preamble, 2))


for i in range(len(numbers)-preamble_length):
    if not is_valid(numbers[i:i+preamble_length], numbers[i+preamble_length]):
        print("number at " + str(i) + ": " + str(numbers[i+preamble_length]))
        break
