n = int(input())
fib = 1
prev1 = 1
prev2 = 0
for i in range(3, n + 1):
    prev2 = prev1
    prev1 = fib
    fib = prev1 + prev2
if n == 0:
    print(0)
else:
    print(fib)