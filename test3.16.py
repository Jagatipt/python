P = int(input())
X = int(input())
Y = int(input())
a = X * 100 + Y
b = a + (a * P / 100)
c = int(b // 100)
d = int(b % 100)
print(c, d)