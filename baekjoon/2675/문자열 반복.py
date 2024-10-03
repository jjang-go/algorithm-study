from sys import stdin as si

N = int(si.readline().rstrip())

for _ in range(0,N):
    C, W = map(str, si.readline().split())
    c = int(C)
    
    for w in W:
        for _ in range(0,c):
            print(w,end="")
    print()