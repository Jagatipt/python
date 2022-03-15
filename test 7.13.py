a = [int(s) for s in input().split()]
b = 0
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            b += 1
print(b)