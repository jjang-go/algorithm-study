from sys import stdin as si

N = int(si.readline().rstrip())

for i in range(1,10):
    print("{0} * {1} = {2}".format(N, i, N*i))