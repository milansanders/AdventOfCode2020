import re

nb_valids = 0
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
present_fields = {}
hcl_pattern = re.compile('^#[0-9a-f]{6}$')
ecl_pattern = re.compile('^(amb|blu|brn|gry|grn|hzl|oth)$')
pid_pattern = re.compile('^[0-9]{9}$')


def all_fields_present(fields: dict):
    missing_fields = required_fields.copy()
    for field in fields.keys():
        if field in missing_fields:
            missing_fields.remove(field)
    return len(missing_fields) == 0


def validate(key, value):
    valid = True
    if key == "byr":
        valid = 1920 <= int(value) <= 2002
    elif key == "iyr":
        valid = 2010 <= int(value) <= 2020
    elif key == "eyr":
        valid = 2020 <= int(value) <= 2030
    elif key == "hgt":
        if value.endswith("cm"):
            valid = 150 <= int(value.split("cm")[0]) <= 193
        elif value.endswith("in"):
            valid = 59 <= int(value.split("in")[0]) <= 76
        else:
            valid = False
    elif key == "hcl":
        valid = bool(hcl_pattern.match(value))
    elif key == "ecl":
        valid = bool(ecl_pattern.match(value))
    elif key == "pid":
        valid = bool(pid_pattern.match(value))
    print((key, value, valid))
    return valid


def do_check():
    global nb_valids, present_fields
    print("present fields: " + str(present_fields))
    valid = all_fields_present(present_fields)
    if valid:
        for field in present_fields:
            if not validate(field, present_fields[field]):
                valid = False
    else:
        print("Not all fields present")
    if valid:
        nb_valids += 1
    present_fields = {}


for line in open('input.txt', 'r').readlines():
    if len(line) == 1:
        do_check()
    else:
        for pair in line.split(" "):
            (k, v) = pair.rstrip().split(":")
            present_fields[k] = v
do_check()

print("\nValid passports: " + str(nb_valids))
