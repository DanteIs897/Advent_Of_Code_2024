from collections import Counter

with open('day_1.txt') as f:
    d = [list(map(int, x.split())) for x in f]

c1, c2 = sorted(x[0] for x in d), sorted(x[1] for x in d)
print(f"Answer 1: {sum(abs(a - b) for a, b in zip(c1, c2))}")
print(f"Answer 2: {sum(k * v for k, v in Counter(c2).items() if k in c1)}")
