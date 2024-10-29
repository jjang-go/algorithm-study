from sys import stdin as si

N, k = map(int, si.readline().split())

L = list(map(int,si.readline().split()))

L.sort(reverse=True)

print(L[k-1])