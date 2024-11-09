from sys import stdin as si

L = []

def dfs(y, x, N):
    if y < 0 or x < 0 or y >= N or x >= N:
        return 0
    
    if L[y][x] == '0':
        return 0
    
    L[y][x] = '0'
    cnt = 1

    cnt += dfs(y + 1, x, N)
    cnt += dfs(y - 1, x, N)
    cnt += dfs(y, x + 1, N)
    cnt += dfs(y, x - 1, N)

    return cnt


N = int(si.readline().rstrip())

for _ in range(N):
    L.append(list(si.readline().rstrip()))

result = []

for y in range(N):
    for x in range(N):
        if L[y][x] == '1':
            result.append(dfs(y, x, N))

print(len(result))
for count in sorted(result):
    print(count)