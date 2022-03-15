from collections import defaultdict
from sys import stdin
 
c = defaultdict(lambda: defaultdict(int))
for line in stdin.readlines():
    v, j, u = line.split()
    c[v][j] += int(u)
         
for v in sorted(c):
    print(v + ':')
    for j in sorted(c[v]):
        print(j, c[v][j])