from sys import stdin as si

N = int(si.readline().rstrip())

D = {}

L = list(map(int,si.readline().split()))

for i in range(0, N):
    if str(L[i]) in D:
        D[str(L[i])] += 1
    else:
        D[str(L[i])] = 1

M = int(si.readline().rstrip())

LL = list(map(int, si.readline().split()))

for i in range(0, M):
    if str(LL[i]) in D:
        print(D[str(LL[i])], end=" ")
    else:
        print(0, end=" ")