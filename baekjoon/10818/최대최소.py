from sys import stdin as si

N = int(si.readline().rstrip())

min_num = 1000001
max_num = -1000001

arr = list(map(int,si.readline().split()))

for i in arr:
    min_num = min(min_num,i)
    max_num = max(max_num,i)
    
print("{0} {1}".format(min_num, max_num))