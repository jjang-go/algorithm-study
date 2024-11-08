from sys import stdin as si
from sys import setrecursionlimit as srl

srl(10000)

N = int(si.readline().rstrip())
T = int(si.readline().rstrip())

L = [[0 for _ in range(N+1)] for _ in range(N+1)]

def dfs(y, x, N):
    if y >= N and x >= N and L[y][0] == 1:
        return
    
    L[y][0] = L[0][y] = 1
    
    for i in range(1, N):
        if L[y][i] == 1 and L[0][i] == 0:
            dfs(i, 1, N)

    return

for _ in range(T):
    x, y = map(int, si.readline().split())
    L[x][y] = L[y][x] = 1
    
dfs(1, 1, N+1)

print(sum(L[0]) - 1)