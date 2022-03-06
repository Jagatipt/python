from math import sqrt

summ = 0
sum_squares = 0
i = int(input())
n = 0
while i != 0:
    n += 1
    summ += i
    sum_squares += i ** 2
    i = int(input())
print(sqrt((sum_squares - summ** 2 / n) / (n - 1)))
