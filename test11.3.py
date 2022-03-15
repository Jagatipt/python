v = {}
for _ in range(int(input())):
    c, b = input().split()
    v[c] = v.get(c, 0) + int(b)
 
for c, b in sorted(v.items()):
    print(c, b)