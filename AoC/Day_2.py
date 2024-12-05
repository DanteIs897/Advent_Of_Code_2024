import sys

D = open(sys.argv[1] if len(sys.argv) > 1 else 'Day_2.txt').read().strip()

def is_good(xs):
    return xs in (sorted(xs), sorted(xs, reverse=True)) and all(1 <= abs(xs[i] - xs[i+1]) <= 3 for i in range(len(xs) - 1))

print(
    sum(is_good(x := list(map(int, l.split()))) for l in D.split('\n')),
    sum(any(is_good(x[:i] + x[i+1:]) for i in range(len(x))) for x in map(lambda l: list(map(int, l.split())), D.split('\n')))
)
