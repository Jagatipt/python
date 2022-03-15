N, K = [int(s) for s in input().split()]
c = ['I'] * N
for i in range(K):
    I, r = [int(s) for s in input().split()]
    for j in range(I - 1, r):
        c[j] = '.'
print(''.join(c))
