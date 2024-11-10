from sys import stdin, setrecursionlimit

setrecursionlimit(10000)

N, M = map(int, stdin.readline().split())

L = [[0] * (N + 1) for _ in range(N + 1)]
V = [False] * (N + 1)

def dfs(i):
    V[i] = True
    for x in range(1, N + 1):
        if L[i][x] == 1 and not V[x]:
            dfs(x)

for _ in range(M):
    x, y = map(int, stdin.readline().split())
    L[x][y] = L[y][x] = 1

count = 0
for i in range(1, N + 1):
    if not V[i]:
        count += 1
        dfs(i)

print(count)
