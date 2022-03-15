a = int(input())
b = {}
for i in range(a):
    q, r = input().split()
    b[q] = r
    b[r] = q
print(b[input()])