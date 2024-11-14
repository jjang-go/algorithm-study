from sys import stdin as si

_ = int(si.readline().rstrip())
L = set(map(int, si.readline().split()))

M = int(si.readline().rstrip())

TL = list(map(int, si.readline().split()))

for data in TL:
    if data in L:
        print(1, end=" ")
    else:
        print(0, end=" ")