a = [int(i) for i in input().split()]
x = int(input())
m = 0
while m < len(a) and a[m] >= x:
    m += 1
print(m + 1)
