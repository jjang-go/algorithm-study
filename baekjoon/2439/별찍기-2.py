from sys import stdin as si

N = int(si.readline().rstrip())
for i in range(0,N):
    for _ in range(0,N-i-1):
        print(" ",end="")
        
    for _ in range(0,i+1):
        print("*",end="")
    print()