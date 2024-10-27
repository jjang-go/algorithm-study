from sys import stdin as si

PN = None
                
if __name__ == "__main__":
    M = int(si.readline().rstrip())
    N = int(si.readline().rstrip())
    
    
    PN = [0] * (N + 1)
    
    PN[0] = PN[1] = -1
    
    for i in range(2,N+1):
        if PN[i] == 0:
            PN[i] = 1
            
            j = i + i
            
            for k in range(j, N+1, i):
                PN[k] = -1
    
    sel_prime = []
    
    for i in range(M, N+1):
        if PN[i] == 1:
            sel_prime.append(i)
            
    if len(sel_prime):
        print(f"{sum(sel_prime)}\n{sel_prime[0]}")
    else:
        print(-1)