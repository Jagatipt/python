m = {}
for i in range(int(input())):
    country, *cities = input().split()
    for city in cities:
        m[city] = country
         
for i in range(int(input())):
    print(m[input()])
