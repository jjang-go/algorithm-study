from sys import stdin as si

prime = [0] * 1000001

for i in range(0, 1000001):
    if i == 0 or i == 1:
        prime[i] = -1
        continue
    
    if prime[i] == 0:
        prime[i] = 1
        
    j = i*i
    
    while j < 1000001:
        if prime[j] == 0:
            prime[j] = -1
        j += i

M, N = map(int, si.readline().split())

for i in range(M, N+1):
    if prime[i] == 1:
        print(i)