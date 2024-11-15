from sys import stdin as si

N, M = map(int, si.readline().split())

SET = set()

for _ in range(N):
    SET.add(si.readline().rstrip())
    
cnt = 0
    
for _ in range(M):
    if si.readline().rstrip() in SET:
        cnt += 1
        
print(cnt)