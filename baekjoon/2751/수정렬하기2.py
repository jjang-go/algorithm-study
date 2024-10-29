from sys import stdin as si

N = int(si.readline().rstrip())

L = []

for _ in range(N):
    L.append(int(si.readline().rstrip()))

L.sort()

for data in L:
    print(data)