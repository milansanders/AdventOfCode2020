inp = open('input.txt', 'r').read().split("\n\n")

rules = {rule.split(": ")[0]: tuple(map(int, rule.split(": ")[1].replace(" or ", "-").split("-"))) for rule in inp[0].split("\n")}
print("rules: " + str(rules))

my_ticket = tuple(map(int, inp[1].split("\n")[1].split(",")))
print("my_ticket: " + str(my_ticket))

tickets = list(map(lambda line: tuple(map(int, line.split(","))), inp[2].split("\n")[1:]))
print("tickets: " + str(tickets))

def follows_any_rule(val):
    for rule in rules:
        (a, b, c, d) = rules[rule]
        if a <= val <= b or c <= val <= d:
            return True
    return False

acc = 0
for ticket in tickets:
    for val in ticket:
        acc += val if not follows_any_rule(val) else 0
print("acc: " + str(acc))