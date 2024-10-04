from sys import stdin as si

while True:
    A, B = map(int, si.readline().split())
    
    if A == 0 and A == B:
        break
    
    if A < B:
        if B % A == 0:
            print("factor")
        else:
            print("neither")
    else:
        if A % B == 0:
            print("multiple")
        else:
            print("neither")