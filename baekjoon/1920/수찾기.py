from sys import stdin as si
from sys import setrecursionlimit as srl

srl(10000000)

N = int(si.readline().rstrip())

L = list(map(int, si.readline().split()))

M = int(si.readline().rstrip())

LL = list(map(int, si.readline().split()))

L.sort()

def binary_search(target, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    
    if L[mid] == target:
        return mid
    elif L[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
        
    return binary_search(target, start, end)

for data in LL:
    if binary_search(data, 0, len(L) - 1) == -1:
        print(0)
    else:
        print(1)