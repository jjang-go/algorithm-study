from sys import stdin as si

N, K = map(int, si.readline().split())

prime  = [0] * (N+1)

cnt = 0

for i in range(2, N+1):
    if prime[i] == 0:
       prime[i] = 1
       cnt += 1
    
    if cnt == K:
        print(i)
        break
    
    j = i * i
    while j < N+1:
        if prime[j] == 0:
            prime[j] = 1
            cnt += 1
            
        if cnt == K:
            print(j)
            break
        
        j += i
        
    if cnt == K:
        break