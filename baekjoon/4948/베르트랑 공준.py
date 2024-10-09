from sys import stdin as si

prime = [0] * 246913

for i in range(2, 246913):
    if prime[i] == 0:
        prime[i] = 1
        
    j = i * i
    
    while j < 246913:
        if prime[j] == 0:
            prime[j] = -1
        j += i
        

while True:
    cnt = 0

    N = int(si.readline().rstrip())
    
    if N == 0:
        break
    
    for i in range(N+1, 2 * N + 1):
        if prime[i] == 1:
            cnt += 1
    
    print(cnt)