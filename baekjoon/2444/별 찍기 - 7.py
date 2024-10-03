from sys import stdin as si

N = int(si.readline().rstrip())

for i in range(0,N-1):
    for _ in range(i, N-1):
        print(end=" ")
    
    for _ in range(0, i*2 + 1):
        print("*",end="")
    print()
    
    
for _ in range(0, (N-1)*2 + 1):
    print("*",end="")
print()

for i in range(0,N-1):
    for _ in range(N-1, N+i):
        print(end=" ")
        
    for _ in range(i, (N-1-i)*2 -1 + i):
        print("*",end="")
    print()