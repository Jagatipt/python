i = int(input())
prev = i
count = 0

while i != 0:
    i = int(input())
    if i > prev:
        count += 1 
    prev = i
print(count)