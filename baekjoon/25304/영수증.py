from sys import stdin as si

C = int(si.readline().rstrip())
N = int(si.readline().rstrip())
for _ in range(0,N):
    PP, PC = map(int,si.readline().split())
    C -= PC * PP
    
if C == 0:
    print("Yes")
else:
    print("No")