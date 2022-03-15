a = {}
for word in input().split():
    a[word] = a.get(word, 0) + 1
    print(a[word] - 1, end=' ')