rules = dict()


def parse_values(value_string):
    value_string = value_string.replace(" bags", "").replace(" bag", "")
    value_strings = list(map(lambda val: val.rstrip(), value_string.split(", ")))
    if value_string[0:2] != "no":
        return list(map(lambda val: (int(val.split(" ")[0]), " ".join(val.split(" ")[1:])), value_strings))
    else:
        return []


def must_contain(desired_bag):
    count = 0
    for rule in rules[desired_bag]:
        added_bags = rule[0] * (1 + must_contain(rule[1]))
        count += added_bags
    return count


for line in open('input.txt', 'r').readlines():
    line = line.replace(".", "")
    key = line.split(" bags contain ")[0].rstrip()
    values = parse_values(line.split(" bags contain ")[1])
    rules[key] = values

print(must_contain("shiny gold"))
