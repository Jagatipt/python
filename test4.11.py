N = int(input())
fact_main = 1
fact_lost = 1

for i in range(1, N):
    i = int(input())
    fact_lost *= i


for j in range(1, N+1):
    fact_main *= j

print(fact_main / fact_lost)