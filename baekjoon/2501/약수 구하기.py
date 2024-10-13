from sys import stdin as si

N, K = map(int, si.readline().split())

for i in range(1, N+1):
    if N % i == 0:
        K -= 1
        
    if K == 0:
        print(i)
        break
    
if K != 0:
    print(0)