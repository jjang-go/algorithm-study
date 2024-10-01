from sys import stdin as si

H, M = map(int, si.readline().split())

if M < 45:
    H = H-1
    M = M + 60

M = M - 45
    
if H < 0:
    H = 23
    
print("{0} {1}".format(H, M))