from sys import stdin as si
from sys import setrecursionlimit as srl

srl(1000000)

def F(N):
    if N <= 1:
        return 1
    
    return N * F(N - 1)

print(F(int(si.readline().rstrip())))