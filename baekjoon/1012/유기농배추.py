from sys import stdin as si

# 재귀 깊이 수동으로 늘림
import sys
sys.setrecursionlimit(10**6)

T = int(si.readline().rstrip())

def F(arr, M, N, x, y):
    if x < 0 or y < 0 or x >= M or y >= N:
        return arr, 0
    
    if arr[y][x] == 0 or arr[y][x] == -1:
        return arr, 0
    
    arr[y][x] = -1
    
    arr, _ = F(arr, M, N, x + 1, y)
    arr, _ = F(arr, M, N, x - 1, y)
    arr, _ = F(arr, M, N, x, y + 1)
    arr, _ = F(arr, M, N, x, y - 1)
    
    return arr, 1
    

for _ in range(0,T):
    cnt = 0
    M, N, K = map(int, si.readline().split())
    
    arr = [[0 for _ in range(M)] for _ in range(N)]
    
    for i in range(0, K):
        x, y = map(int, si.readline().split())
        arr[y][x] = 1
        
    for i in range(0, N):
        for j in range(0, M):
            if arr[i][j] == 1:
                arr, tmp = F(arr, M, N, j, i)
                cnt += tmp
        
    print(cnt)