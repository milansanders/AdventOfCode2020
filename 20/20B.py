tiles = []
for tile in open('input.txt', 'r').read().split("\n\n"):
    lines = tile.split("\n")
    tiles.append([int(lines[0][5:-1]), lines[1:]])
monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   ',
]
monster_coords = [(x, y) for y in range(len(monster)) for x in range(len(monster[y])) if monster[y][x] == "#"]


def flip_vert(img):
    return img[::-1]


def flip_horz(img):
    return [line[::-1] for line in img]


def turn_right(img):
    return ["".join([img[y][x] for y in range(len(img) - 1, -1, -1)]) for x in range(len(img[0]))]


def get_top_edge(img):
    return img[0]


def get_bot_edge(img):
    return img[-1]


def get_left_edge(img):
    return "".join([line[0] for line in img])


def get_right_edge(img):
    return "".join([line[-1] for line in img])


def get_edges(tile):
    return [get_right_edge(tile[1]), get_top_edge(tile[1]), get_left_edge(tile[1]), get_bot_edge(tile[1])]


def edge_eq(a, b):
    if a == b:
        return 1
    elif a == b[::-1]:
        return -1
    else:
        return 0


def has_matching_edges(tile_a, tile_b):
    for edge_a in get_edges(tile_a):
        if len(list(filter(lambda edge_b: edge_eq(edge_a, edge_b) != 0, get_edges(tile_b)))) > 0:
            return True
    return False


def get_match(edge):
    for other_tile in tiles:
        for other_edge in get_edges(other_tile):
            if edge_eq(edge, other_edge):
                return other_tile
    return None


def has_any_match(edge):
    return get_match(edge) is not None


def get_any_corner():
    for tile in tiles:
        other_tiles = [t for t in tiles if t[0] != tile[0]]
        if len(list(filter(lambda other_tile: has_matching_edges(tile, other_tile), other_tiles))) == 2:
            return tile
    raise


def spin_and_check(tile, pred):
    for _ in range(4):
        if pred(tile):
            return True
        tile[1] = turn_right(tile[1])
    return False


def manipulate_tile_to_match_edge(edge, edge_extract, tile):
    pred = lambda t: edge_eq(edge, edge_extract(tile[1])) == 1
    if spin_and_check(tile, pred):
        return
    tile[1] = flip_vert(tile[1])
    if spin_and_check(tile, pred):
        return
    tile[1] = flip_horz(tile[1])
    if spin_and_check(tile, pred):
        return
    raise


def is_monster(x, y):
    for (m_x, m_y) in monster_coords:
        (p_x, p_y) = (m_x + x, m_y + y)
        if picture[p_y][p_x] != "#":
            return False
    return True


def highlight_monsters():
    found_monster = False
    for y in range(len(picture) - len(monster)):
        for x in range(len(picture[0]) - len(monster[0])):
            if is_monster(x, y):
                for (m_x, m_y) in monster_coords:
                    (p_x, p_y) = (m_x + x, m_y + y)
                    picture[p_y] = picture[p_y][:p_x] + "0" + picture[p_y][p_x + 1:]
                found_monster = True
    return found_monster


# First make a top-left corner
corner = get_any_corner()
tiles.remove(corner)
while has_any_match(get_top_edge(corner[1])) or has_any_match(get_left_edge(corner[1])):
    corner[1] = turn_right(corner[1])
top_row = [corner]

# Then finish the top row
while (new_right_tile := get_match(right_edge := get_right_edge(top_row[-1][1]))) is not None:
    tiles.remove(new_right_tile)
    manipulate_tile_to_match_edge(right_edge, get_left_edge, new_right_tile)
    top_row.append(new_right_tile)

# Finish full img
full_img = [top_row]
while (new_bot_tile := get_match(bot_edge := get_bot_edge(full_img[-1][0][1]))) is not None:
    new_row = [new_bot_tile]
    tiles.remove(new_bot_tile)
    manipulate_tile_to_match_edge(bot_edge, get_top_edge, new_bot_tile)
    while (new_right_tile := get_match(right_edge := get_right_edge(new_row[-1][1]))) is not None:
        tiles.remove(new_right_tile)
        manipulate_tile_to_match_edge(right_edge, get_left_edge, new_right_tile)
        new_row.append(new_right_tile)
    full_img.append(new_row)

# Build picture
picture = []
for row in full_img:
    imgs = list(map(lambda tile: ["".join([c for c in line[1:-1]]) for line in tile[1][1:-1]], row))
    for i in range(len(imgs[0])):
        picture.append("".join(list(map(lambda img: img[i], imgs))))

# Highlight monsters
if not highlight_monsters():
    picture = turn_right(flip_vert(picture))
    highlight_monsters()
print("\nMonsters:")
for line in picture:
    print(line)

print("Roughness: " + str(len(list(filter(lambda char: char == "#", list("".join(picture)))))))
