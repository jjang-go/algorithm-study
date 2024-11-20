from sys import stdin as si

N, M = map(int, si.readline().split())

S = set(list())

for _ in range(N):
    S.add(si.readline().rstrip())

cnt = 0
L = []

for _ in range(M):
    tmp = si.readline().rstrip()
    if tmp in S:
        cnt += 1
        L.append(tmp)

L.sort()

print(cnt)
for data in L:
    print(data)