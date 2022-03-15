def p(a, i, j):
    for z in range(len(a)):
        a[z][i], a[z][j] = a[z][j], a[z][i]
n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
i, j = [int(i) for i in input().split()]
p(a, i, j)
for o in a:
    for z in o:
        print(z, end=" ")
    print()