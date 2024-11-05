from sys import stdin as si

L = list(map(int, si.readline().split()))

L.sort()

print(L[1])