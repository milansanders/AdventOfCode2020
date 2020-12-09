import itertools

numbers: [int] = list(map(lambda line: int(line.rstrip()), open('input.txt', 'r').readlines()))
preamble_length: int = 25


def is_valid(preamble: [int], target: int) -> bool:
    return target in map(sum, itertools.combinations(preamble, 2))


def invalid_number(numbers: [int], preamble_length: int) -> int:
    for i in range(len(numbers)-preamble_length):
        if not is_valid(numbers[i:i+preamble_length], numbers[i+preamble_length]):
            return numbers[i+preamble_length]


def contig_ends(numbers: [int], target: int) -> int:
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            acc = sum(numbers[i:j])
            if acc == target:
                contig_list = numbers[i:j]
                return min(contig_list)+max(contig_list)
            elif acc > target:
                break


invalid_number = invalid_number(numbers, preamble_length)
print(contig_ends(numbers, invalid_number))
