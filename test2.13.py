N = int(input())
M = int(input())
x = int(input())
y = int(input())

if(N > M):
    print(min(x, y, M - x, N - y))
else:
    print(min(x, y, N - x, M - y))