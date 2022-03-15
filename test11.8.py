from collections import defaultdict
l = defaultdict(list)
for i in range(int(input())):
    x, f = input().split(' - ')
    z = f.split(', ')
    for w in z:
        l[w].append(x)
print(len(l))
for w, g in sorted(l.items()):
    print(w + ' - ' + ', '.join(g))