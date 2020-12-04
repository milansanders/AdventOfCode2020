nb_valids = 0
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
missing_fields = required_fields.copy()

def do_check():
    global nb_valids, missing_fields
    print("missing fields: " + str(missing_fields))
    if len(missing_fields) == 0:
        print("VALID")
        nb_valids += 1
    else:
        print("INVALID")
    missing_fields = required_fields.copy()

for line in open('input.txt', 'r').readlines():
    if len(line) == 1:
        do_check()
    else:
        present_fields = list(map(lambda pair: pair.split(":")[0], line.split(" ")))
        print(present_fields)
        for field in present_fields:
            if field in missing_fields:
                missing_fields.remove(field)
do_check()

print(nb_valids)
