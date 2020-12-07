rules = dict()


def parse_values(value_string):
    value_string = value_string.replace(" bags", "").replace(" bag", "")
    value_strings = list(map(lambda val: val.rstrip(), value_string.split(", ")))
    if value_string[0:2] != "no":
        return list(map(lambda val: (int(val.split(" ")[0]), " ".join(val.split(" ")[1:])), value_strings))
    else:
        return []


def can_contain(desired_bag):
    bags = set()
    for bag in rules:
        for i in list(filter(lambda b: b[1] == desired_bag, rules[bag])):
            bags.add(bag)
            for j in can_contain(bag):
                bags.add(j)
    return bags


for line in open('input.txt', 'r').readlines():
    line = line.replace(".", "")
    key = line.split(" bags contain ")[0].rstrip()
    values = parse_values(line.split(" bags contain ")[1])
    rules[key] = values

print(len(can_contain("shiny gold")))
