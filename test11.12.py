def z(m, o):
    if m == o:
        return True
    while m in x:
        m = x[m]
        if m == o:
            return True
    return False
     
x = dict()
n = int(input())
for i in range(n - 1):
    child, parent = input().split()
    x[child] = parent
 
for i in range(int(input())):
    first, second = input().split()
    if z(second, first):
        print(1, end=' ')
    elif z(first, second):
        print(2, end=' ')
    else:
        print(0, end=' ')