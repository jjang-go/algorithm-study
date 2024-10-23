from sys import stdin as si

T = int(si.readline().rstrip())

while T >= 1:
    T -= 1
    L = list(si.readline())
    
    tmp = []
    
    for data in L:
        if data == '(':
            tmp.append(data)
        elif data == ')':
            if tmp:
                tmp.pop()
            else:
                print("NO")
                break
        else:
            if tmp:
                print("NO")
            else:
                print("YES")