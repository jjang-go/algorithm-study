from sys import stdin as si

T = int(si.readline().rstrip())

arr = [0] * T

for i in range(0,T):
    arr[i] = int(si.readline().rstrip())
    
arr.sort()

for i in range(0,T):
    print(arr[i])