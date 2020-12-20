from functools import reduce

def get_edges(tile):
    edges = []
    edges.append(tile[0])
    edges.append(tile[-1])
    edges.append("".join([line[0] for line in tile]))
    edges.append("".join([line[-1] for line in tile]))
    return edges


def edge_eq(a, b):
    return a == b or a == b[::-1]


def nb_matching_edges(edges_a, edges_b):
    for edge_a in edges_a:
        if len(list(filter(lambda edge_b: edge_eq(edge_a, edge_b), edges_b))) > 0:
            return True
    return False


inp = open('input.txt', 'r').read().split("\n\n")
tiles = []
for i in inp:
    lines = i.split("\n")
    tiles.append((int(lines[0][5:-1]), get_edges(lines[1:])))

corner_ids = []
for i in range(len(tiles)):
    tile = tiles[i]
    other_edges = [t[1] for j, t in enumerate(tiles) if j != i]
    match_count = 0
    for other_edge in other_edges:
        nb_match = nb_matching_edges(tile[1], other_edge)
        if nb_match:
            match_count += 1
    if match_count == 2:
        corner_ids.append(tile[0])
print("Corners: " + str(corner_ids))

acc = reduce(lambda a, b: a * b, corner_ids)
print("Product of corner IDs: " + str(acc))
