from sys import stdin as si

prime = [0] * 1001

for i in range(0, 1001):
    if i == 0 or i == 1:
        prime[i] = -1
        continue
    
    if prime[i] == 0:
        prime[i] = 1
        
    j = i*i
    
    while j < 1001:
        prime[j] = -1
        j += i
        
N = int(si.readline().rstrip())

L = list(map(int,si.readline().split()))

sum = 0

for i in range(0, N):
    if prime[L[i]] == 1:
        sum += 1
        
print(sum)