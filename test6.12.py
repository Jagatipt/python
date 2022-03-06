i = int(input())
maxi1 = i
maxi2 = 0
prev = i
while i != 0:
    i = int(input())
    if i < prev and i > maxi2:
        maxi2 = i
    if i > prev and i > maxi2 and i < maxi1:
        maxi2 = i
    if i > prev and i > maxi1:
        maxi2 = maxi1
        maxi1 = i
    prev = i
print(maxi2)