def h(m):
    if m not in f:
        return 0
    else:
        return 1 + h(f[m])
 
f = {}
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    f[child] = parent
 
hs = {}
for m in set(f.keys()).union(set(f.values())):
    hs[m] = h(m)
 
for key, value in sorted(hs.items()):
    print(key, value)