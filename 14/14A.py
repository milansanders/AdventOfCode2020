mem = dict()
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def as_bin(val: int) -> str:
    b = bin(val)[2:]
    preamble = "0" * (len(mask)-len(b))
    return preamble + b


def set_char(string, idx, char):
    lst = list(string)
    lst[idx] = char
    return "".join(lst)


def do_mask(val, mask):
    bin_val = as_bin(val)
    print("bin_val: " + bin_val)
    for i in range(len(bin_val)):
        bit = mask[i]
        if not bit == "X":
            bin_val = set_char(bin_val, i, bit)
    print("masked bin_val: " + bin_val)
    new_val = int(bin_val, 2)
    print("masked bin_val: " + str(new_val))
    return new_val


for line in open("input.txt", "r").readlines():
    line = line.rstrip().split(" = ")
    op = line[0]
    val = line[1]
    if op[0:4] == "mask":
        mask = val
        print("mask is now " + mask)
    else:
        masked_val = do_mask(int(val), mask)
        adr = int(op[:-1].split("[")[1])
        mem[adr] = masked_val
        print("mem[%d] = %d" % (adr, masked_val))

print("Total memory values: " + str(sum(mem.values())))
