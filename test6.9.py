maxi = 0
ind = -2
i = -1
len = 0

while i != 0:
    i = int(input())
    if i > maxi:
        maxi = i
        ind = len
        
    len += 1
    
print(ind)