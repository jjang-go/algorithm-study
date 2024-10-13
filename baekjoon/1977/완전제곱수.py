from sys import stdin as si

M = int(si.readline().rstrip())
N = int(si.readline().rstrip())

psn = [i*i for i in range(1, int(N**0.5) + 1) if M <= i*i <= N]

if len(psn):
    print(sum(psn))
    print(min(psn))
else:
    print(-1)