from collections import Counter
w = []
for _ in range(int(input())):
    w.extend(input().split())
r = Counter(w)
p = [(-p[1], p[0]) for p in r.most_common()]
w = [p[1] for p in sorted(p)]
print('\n'.join(w))