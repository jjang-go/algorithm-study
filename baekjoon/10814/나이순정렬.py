from sys import stdin as si

N = int(si.readline().rstrip())

L = []

for _ in range(N):
    A,B = map(str, si.readline().split())
    L.append((int(A),B))

L.sort(key=lambda x: int(x[0]))

for data in L:
    print(data[0], data[1])