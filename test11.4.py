c = {}
for i in range(int(input())):
    w = input().split()
    for word in w:
        c[word] = c.get(word, 0) + 1
         
max_count = max(c.values())
most_frequent = [k for k, v in c.items() if v == max_count]
print(min(most_frequent))