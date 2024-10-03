from sys import stdin as si
L1 = [1,1,2,2,2,8]
L2 = list(map(int,si.readline().split()))

for i in range(0,6):
    print(L1[i] - L2[i], end=" ")