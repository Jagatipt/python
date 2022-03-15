a = [int(s) for s in input().split()]
x, y = [int(s) for s in input().split()]
 
a.append(0)
for i in range(len(a) - 1, x, -1):
    a[i] = a[i - 1]
a[x] = y
print(' '.join([str(i) for i in a]))
