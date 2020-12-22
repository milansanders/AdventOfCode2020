from functools import reduce

decks = list(map(lambda deck: list(map(int, deck.split("\n")[1:])), open('input.txt', 'r').read().split("\n\n")))
print(decks)
round = 1
while len(list(filter(lambda deck: len(deck) > 0, decks))) > 1:
    print("-- Round %d --" % round)
    for p, d in enumerate(decks):
        print("Player %d's deck: %s" % (p + 1, ", ".join(map(str, d))))
    plays = list(map(lambda deck: deck.pop(0), decks))
    for p, c in enumerate(plays):
        print("Player %d plays: %s" % (p + 1, c))
    winner = plays.index(max(plays))
    print("Player %d wins the round!\n" % (winner + 1))
    plays.sort()
    decks[winner] += plays[::-1]
    round += 1
score = sum(map(lambda a: a[0] * a[1], zip(reduce(lambda a, b: a + b, decks), range(sum(map(len, decks)), 0, -1))))
print("Score: " + str(score))
