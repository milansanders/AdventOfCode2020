def transform(sub, loops):
    val = 1
    for _ in range(loops):
        val = (val * sub) % 20201227
    return val


def get_loop(pub):
    loop = 0
    val = 1
    while pub != val:
        loop += 1
        if (loop % 1000000) == 0:
            print("\n-- loop %d --" % loop)
        val = (val * 7) % 20201227
    return loop


# pub_card, pub_door = 5764801, 17807724  # Test
pub_card, pub_door = 8184785, 5293040  # Input
loop_card = get_loop(pub_card)
print("Loop number of card: %d" % loop_card)
key = transform(pub_door, loop_card)
print("Room key: %d" % key)