a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

if b1 == a1 or b2 == a2 or abs(b1 - a1) == abs(b2-a2):
    print("YES")
else:
    print("NO")