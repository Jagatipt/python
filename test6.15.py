A = int(input())
fib = 1
prev1 = 1
prev2 = 0
count = 2  
while fib < A:
    prev2 = prev1
    prev1 = fib
    fib = prev1 + prev2
    count += 1
if fib == A:
    print(count)
else:
    print(-1)