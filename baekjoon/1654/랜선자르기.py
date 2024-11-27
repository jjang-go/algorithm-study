from sys import stdin as si

K, N = map(int, si.readline().split())

L = [int(si.readline().rstrip()) for _ in range(K)]

start, end = 1, max(L)

while start <= end:
    mid, cnt = (start + end) // 2, 0
    
    for i in L:
        cnt += i // mid
    if cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)