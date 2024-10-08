from sys import stdin as si
from math import lcm

T = int(si.readline().rstrip())

for _ in range(0, T):
    A, B = map(int,si.readline().split())
    print(lcm(A,B))