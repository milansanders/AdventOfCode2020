lines = open('input.txt', 'r').readlines()
boarding_passes = map(lambda line: line.rstrip(), lines)
binary_passes = map(lambda line: line.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0"), boarding_passes)
seat_ids = set(map(lambda seat: int(seat, 2), binary_passes))
max_id = max(seat_ids)

possible_seats = []
for seat in range(max_id):
    if (seat-1) in seat_ids and (seat+1) in seat_ids and seat not in seat_ids:
        possible_seats.append(seat)
print("Possible seats: " + str(possible_seats))
