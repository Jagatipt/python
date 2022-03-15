st = input()
c = ''
for i in range(len(st)):
    if i % 3 != 0:
        c = c + st[i]
print(c)
