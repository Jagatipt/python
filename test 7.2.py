a = [int(s) for s in input().split()]
print(*[k for k in a if k % 2 ==0])