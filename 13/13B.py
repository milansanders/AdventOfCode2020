from functools import reduce
from itertools import combinations

inp = open('input.txt', 'r').readlines()[1].split(",")
a = []
n = []
for i in range(len(inp)):
    line = inp[i]
    if not line == "x":
        line = int(line)
        a.append(-i % line)
        n.append(line)
print("Lines: " + str(list(zip(a, n))))


# lines are a set of tuples of form (a_i, n_i) with n_i = busId and a_i = -delay mod busId
# system of congruences x ≡ a_i (mod n_i)
def solve_congruences(a, n):
    N = reduce(lambda p, q: p * q, n)
    x = 0
    for a_i, n_i in zip(a, n):
        y_i = N / n_i
        z_i = mult_inv(y_i, n_i)
        x += a_i * y_i * z_i
    return x % N


def mult_inv(a, b):
    a0, b0 = a, b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    res = x1 % b0
    return res


def is_coprime(p, q):
    while q != 0:
        p, q = q, p % q
    return p == 1


def valid_t(t, a, n):
    valid = True
    for a_i, n_i in zip(a, n):
        mod = (t - a_i) % n_i
        if not mod == 0:
            print("bus %d departed %dm ago" % (n_i, mod))
            valid = False
    return valid


print()
print("First checking if all the factors are co-prime...")
all_n_coprime = True
for c in combinations(n, 2):
    if not is_coprime(c[0], c[1]):
        print("%d and %d are not co-prime" % (c[0], c[1]))
        all_n_coprime = False
if all_n_coprime:
    print("All factors are co-prime")
print()

t_0 = solve_congruences(a, n)
print("%d valid? %s" % (t_0, valid_t(t_0, a, n)))

# I got pretty close at the start figuring out it's a system of congruences and it works on all the test cases
# But for some reason the answer is consistently off by 10 for the actual input (on over 600 quadrillion)
t_0 = t_0 - 10
print("%d valid? %s" % (t_0, valid_t(t_0, a, n)))
