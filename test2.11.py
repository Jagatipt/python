a1 = int(input())
a2 = int(input())
b1 = int(input())
b2 = int(input())

if abs(b1 - a1)**2 + abs(b2-a2)**2 == 5:
	print("YES")
else:
	print("NO")