i = int(input())
count = 0
maxi = 0
while i != 0:
    if i > maxi:
        maxi = i
        count = 1
    elif i == maxi:
        count += 1
    i = int(input())
print(count)