from sys import stdin as si

L = []

for _ in range(0, 5):
    L.append(int(si.readline().rstrip()))

print(sum(L)//5)
    
L.sort()

print(L[2])
