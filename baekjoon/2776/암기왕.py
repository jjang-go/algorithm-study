from sys import stdin as si
from sys import setrecursionlimit as srl

srl(100000000)

T = int(si.readline().rstrip())

def binary_search(L, target, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    
    if L[mid] == target:
        return mid
    elif L[mid] > target:
        return binary_search(L, target, start, mid - 1)
    else:
        return binary_search(L, target, mid + 1, end)

while T:
    T -= 1
    
    _ = si.readline()
    
    L = sorted(list(map(int, si.readline().split())))
    
    _ = si.readline()
    
    LL = list(map(int, si.readline().split()))
    
    for data in LL:
        if binary_search(L, data, 0, len(L) - 1) == -1:
            print(0)
        else:
            print(1)