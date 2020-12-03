treeMap = open('input.txt', 'r').readlines()
edge = len(treeMap)
steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
result = 1


def has_tree(pos):
    treeLine = treeMap[pos[1]].rstrip()
    return treeLine[pos[0] % len(treeLine)] == "#"


def get_trees(step):
    nbTrees = 0
    pos = (0, 0)
    while pos[1] < edge:
        tree = has_tree(pos)
        if (tree):
            nbTrees += 1
        pos = pos[0] + step[0], pos[1] + step[1]
    return nbTrees


for step in steps:
    nbTrees = get_trees(step)
    print(str(step) + ": " + str(nbTrees))
    result *= nbTrees
print(result)
