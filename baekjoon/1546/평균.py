from sys import stdin as si

N = int(si.readline().strip())

List = list(map(int, si.readline().split()))

M = max(List)

sum = 0

for data in List:
    sum += data / M * 100
    
print(sum / N)