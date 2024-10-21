from collections import deque
from sys import stdin as si

T = int(si.readline().rstrip())

D = deque()

while T >= 1:
    T -= 1
    
    tmp = si.readline().split()
    
    if tmp[0] == "push_front":
        D.appendleft(tmp[1])
    elif tmp[0] == "push_back":
        D.append(tmp[1])
    elif tmp[0] == "size":
        print(len(D))        
    elif tmp[0] == "empty":
        if D:
            print(0)
        else:
            print(1)
    elif tmp[0] == "front":
        if D:
            print(D[0])
        else:
            print(-1)
    elif tmp[0] == "back":
        if D:
            print(D[len(D)-1])
        else:
            print(-1)
    elif tmp[0] == "pop_front":
        if D:
            print(D[0])    
            D.popleft()
        else:
            print("-1")
    elif tmp[0] == "pop_back":
        if D:
            print(D[len(D) - 1])    
            D.pop()
        else:
            print("-1")