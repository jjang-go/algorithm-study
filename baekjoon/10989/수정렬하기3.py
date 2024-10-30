from sys import stdin as si

N = int(si.readline().rstrip())

line = [0] * (10001)

for _ in range(0,N):
    line[int(si.readline().rstrip())] += 1

cnt = 0

for i in range(0,len(line)):
    if cnt == N:
        break
    
    if line[i] != 0:
        for _ in range(line[i]):
            print(i)