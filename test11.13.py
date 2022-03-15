def a(b, c):
    result = []
    result.append(b)
    while b in c:
        b = c[b]
        result.append(b)
    return result
 
c = dict()
n = int(input())
for i in range(n - 1):
    b, parent = input().split()
    c[b] = parent
     
m = int(input())
for i in range(m):
    b_1, b_2 = input().split()
    a_for_1 = set(a(b_1, c))
    for ancestor in a(b_2, c):
        if ancestor in a_for_1:
            print(ancestor)
            break