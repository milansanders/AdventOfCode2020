nbTrees = 0
pos = (0, 0)
step = (3, 1)
treeMap = open('input.txt', 'r').readlines()
edge = len(treeMap)

def has_tree(pos):
    treeLine = treeMap[pos[1]].rstrip()
    return treeLine[pos[0] % len(treeLine)] == "#"

while pos[1] < edge:
    tree = has_tree(pos)
    if (tree):
        nbTrees += 1
    pos = pos[0] + step[0], pos[1] + step[1]
print(nbTrees)
