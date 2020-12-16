inp = open('input.txt', 'r').read().split("\n\n")

rules = {rule.split(": ")[0]: tuple(map(int, rule.split(": ")[1].replace(" or ", "-").split("-"))) for rule in
         inp[0].split("\n")}

my_ticket = tuple(map(int, inp[1].split("\n")[1].split(",")))

tickets = list(map(lambda line: tuple(map(int, line.split(","))), inp[2].split("\n")[1:]))


def all_follow_rule(vals, rule):
    for val in vals:
        (a, b, c, d) = rule
        if val < a or b < val < c or d < val:
            return False
    return True


def follows_any_rule(val):
    for rule in rules:
        (a, b, c, d) = rules[rule]
        if a <= val <= b or c <= val <= d:
            return True
    return False


def valid_ticket(ticket):
    for val in ticket:
        if not follows_any_rule(val):
            return False
    return True


valid_tickets = list(filter(valid_ticket, tickets))

possible_rule_order = []
for i in range(len(my_ticket)):
    vals = list(map(lambda t: t[i], valid_tickets))
    possible_rules = []
    for rule_name in rules:
        rule = rules[rule_name]
        if all_follow_rule(vals, rule):
            possible_rules.append(rule_name)
    possible_rule_order.append(possible_rules)


def all_rules_determined(possible_rule_order):
    return len(list(filter(lambda possible_rules: len(possible_rules) > 1, possible_rule_order))) == 0


while not all_rules_determined(possible_rule_order):
    for rule in filter(lambda possible_rules: len(possible_rules) == 1, possible_rule_order):
        rule = rule[0]
        for possible_rules in filter(lambda possible_rules: len(possible_rules) > 1, possible_rule_order):
            if rule in possible_rules:
                possible_rules.remove(rule)

possible_rule_order = list(map(lambda rules: rules[0], possible_rule_order))
prefix = "departure"
acc = 1
for i in range(len(my_ticket)):
    if possible_rule_order[i].startswith(prefix):
        acc *= my_ticket[i]
print("acc: " + str(acc))
