N = int(input())
i = 1
count = 0
while i <= N:
    i *= 2
    count += 1
print(count - 1, i / 2)