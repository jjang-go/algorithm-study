from sys import stdin as si

N = int(si.readline().rstrip())

for i in range(1, N+1):
    for _ in range(0,i):
        print("*",end="")
    print()