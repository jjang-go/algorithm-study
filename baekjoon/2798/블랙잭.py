from sys import stdin as si

N, M = map(int, si.readline().split())

arr = list(map(int,si.readline().split()))


max_num = 0
for i in range(0, N):
    for j in range(0, N):
        if i == j:
            continue
        
        for k in range(0, N):
            if i == k or j == k:
                continue
            
            if arr[i] + arr[j] + arr[k] <= M:
                max_num = max(max_num, arr[i] + arr[j] + arr[k])
    
print(max_num)