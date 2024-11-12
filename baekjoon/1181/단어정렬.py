from sys import stdin as si

N = int(si.readline().rstrip())

L = sorted(sorted(list(set([si.readline().rstrip() for _ in range(N)]))), key=len)

for l in L:
    print(l)