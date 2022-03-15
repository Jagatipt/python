n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
v, b = 0, 0
max = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > max:
            max = a[i][j]
            v, b = i, j
print(v, b)