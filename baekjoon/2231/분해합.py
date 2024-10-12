from sys import stdin as si

N = int(si.readline().rstrip())

for i in range(1, 1000000):
    sum = i
    
    for j in str(i):
        sum += int(j)
        
    if sum == N:
        print(i)
        break
    
    if i == 999999:
        print(0)