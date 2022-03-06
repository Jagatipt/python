i = int(input())
prev = i
count = 1 
count_max = count
while i != 0:
    i = int(input())
    if i == prev:
        count += 1
    else:
        count = 1
    if count > count_max:
        count_max = count 
    prev = i
print(count_max)