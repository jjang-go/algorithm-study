from sys import stdin as si

L = []

N = int(si.readline().rstrip())

for _ in range(0, N):
    L.append(list(map(int,si.readline().split())))
    
L.sort()

for i in L:
    print(i[0], i[1])