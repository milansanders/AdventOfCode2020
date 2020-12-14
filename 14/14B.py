mem = dict()
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


def as_bin(val: int, length=len(mask)) -> str:
    b = bin(val)[2:]
    preamble = "0" * (length-len(b))
    return preamble + b


def set_char(string, idx, char):
    lst = list(string)
    lst[idx] = char
    return "".join(lst)


def do_mask(adr, mask):
    bin_adr = as_bin(adr)
    for i in range(len(bin_adr)):
        bit = mask[i]
        if not bit == "0":
            bin_adr = set_char(bin_adr, i, bit)
    return bin_adr


def expand_adr(masked_adr):
    x_idx = [i for i, x in enumerate(masked_adr) if x == "X"]
    adrs = []
    for i in range(2 ** len(x_idx)):
        act_adr = masked_adr
        num = as_bin(i, len(x_idx))
        for i in range(len(x_idx)):
            act_adr = set_char(act_adr, x_idx[i], list(num)[i])
        adrs.append(int(act_adr, 2))
    return adrs


for line in open("input.txt", "r").readlines():
    line = line.rstrip().split(" = ")
    op = line[0]
    val = line[1]
    if op[0:4] == "mask":
        mask = val
    else:
        val = int(val)
        adr = int(op[:-1].split("[")[1])
        masked_adr = do_mask(int(adr), mask)
        for act_adr in expand_adr(masked_adr):
            mem[act_adr] = val

print("Total memory values: " + str(sum(mem.values())))
