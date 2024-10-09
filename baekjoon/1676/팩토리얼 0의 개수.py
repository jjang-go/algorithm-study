from sys import stdin as si

def F(n):
    if n <= 1:
        return 1
    
    return n * F(n - 1)

N = int(si.readline().rstrip())

f = str(F(N))

cnt = 0

for i in range(len(f)-1,0,-1):
    if f[i] != '0':
        break
    
    cnt += 1

print(cnt)