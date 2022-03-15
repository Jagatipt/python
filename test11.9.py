n = int(input())
a = {}
for i in range(n):
    w = input()
    b = w.lower()
    if b not in a:
        a[b] = set()
    a[b].add(w)
z = 0
sent = input().split()
for w in sent:
    b = w.lower()
    if (b in a and w not in a[b]
            or len([l for l in w if l.isupper()]) != 1):
        z += 1
print(z)