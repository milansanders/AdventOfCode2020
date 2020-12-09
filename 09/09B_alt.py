import itertools

numbers: [int] = list(map(lambda line: int(line.rstrip()), open('input.txt', 'r').readlines()))
preamble_length: int = 25


def is_valid(preamble: [int], target: int) -> bool:
    return target in map(sum, itertools.combinations(preamble, 2))


def invalid_number(numbers: [int], preamble_length: int) -> int:
    for i in range(len(numbers)-preamble_length):
        if not is_valid(numbers[i:i+preamble_length], numbers[i+preamble_length]):
            return numbers[i+preamble_length]


def contig_ends_crawl(numbers: [int], target: int) -> int:
    (i, j) = (0, 1)
    acc = numbers[i] + numbers[j]
    while acc != target:
        if acc < target:
            j += 1
            acc += numbers[j]
        elif acc > target:
            acc -= numbers[i]
            i += 1
    contig_list = numbers[i:j]
    return min(contig_list) + max(contig_list)


invalid_number = invalid_number(numbers, preamble_length)
print("invalid number: " + str(invalid_number))
print("min+max of contig list: " + str(contig_ends_crawl(numbers, invalid_number)))
