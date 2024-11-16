from sys import stdin as si

D = {}

N, M = map(int, si.readline().split())

for i in range(1, N + 1):
    monster = si.readline().rstrip()
    D[monster] = str(i)
    D[str(i)] = monster
    
for _ in range(M):
    q = str(si.readline().rstrip())
    print(D[q])