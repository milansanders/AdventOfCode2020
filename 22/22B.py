from functools import reduce

decks = list(map(lambda deck: list(map(int, deck.split("\n")[1:])), open('input.txt', 'r').read().split("\n\n")))


def play_game(decks, game_count):
    print("=== Game %d ===" % game_count)
    states = []
    round = 1
    winner = -1
    while len(list(filter(lambda deck: len(deck) > 0, decks))) > 1:
        print("\n-- Round %d (Game %d) --" % (round, game_count))
        for p, d in enumerate(decks):
            print("Player %d's deck: %s" % (p + 1, ", ".join(map(str, d))))
        state = "".join(map(str, reduce(lambda a, b: a + [-1] + b, decks)))
        if state in states:
            print("State has already been reached, player 1 wins!")
            winner = 0
            break
        else:
            states.append(state)
        plays = list(map(lambda deck: deck.pop(0), decks))
        for p, c in enumerate(plays):
            print("Player %d plays: %s" % (p + 1, c))

        if len(list(filter(lambda a: len(a[1]) < a[0], zip(plays, decks)))) > 0:
            winner = plays.index(max(plays))
            plays.sort()
            plays = plays[::-1]
        else:
            print("Playing a sub-game to determine the winner...\n")
            game_count += 1
            winner = play_game(list(map(lambda a: a[1][:a[0]], zip(plays, decks))), game_count + 1)
            if winner == 1:
                plays = plays[::-1]
        print("Player %d wins round %d of game %d!" % (winner + 1, round, game_count + 1))
        decks[winner] += plays
        round += 1
    print("The winner of game %d is player %d!\n" % (game_count, winner + 1))
    assert winner >= 0
    if game_count > 0:
        print("...anyway, back to game %d." % (game_count - 1))
    return winner


winner = play_game(decks, 1)
print("\n== Post-game results ==")
for p, d in enumerate(decks):
    print("Player %d's deck: %s" % (p + 1, ", ".join(map(str, d))))
score = sum(map(lambda a: a[0] * a[1], zip(decks[winner], range(sum(map(len, decks)), 0, -1))))
print("\nPlayer %d won with a score of %d" % (winner + 1, score))
