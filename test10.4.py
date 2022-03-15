s = [int(s) for s in input().split()]
A = set()
for elm in s:
    if elm in A:
        print('YES')
    else:
        A.add(elm)
        print('NO')