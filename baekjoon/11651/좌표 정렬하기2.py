from sys import stdin as si

L = []

N = int(si.readline().rstrip())

for i in range(0, N):
    x, y = map(int, si.readline().split())
    L.append((x, y))

L.sort(key=lambda item: (item[1], item[0]))

for item in L:
    print(item[0], item[1])