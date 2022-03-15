N, M = [int(s) for s in input().split()]
A = set()
B = set()
for i in range(N):
    A.add(int(input()))
for j in range(M):
    B.add(int(input()))
X1 = sorted(A.intersection(B))
print(len(X1)) 
for elem in list(X1):
    print(elem, end=' ')

X2 = sorted(A.difference(B))
print(len(X2)) 
for elem in list(X2):
    print(elem, end=' ')
    
X3 = sorted(B.difference(A))
print(len(X3)) 
for elem in list(X3):
    print(elem, end=' ')

\\у меня почему-то не работали операторы над множествами, пришлось их прописывать 