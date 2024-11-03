from sys import stdin as si

def F(n):
    if n <= 1:
        return 1
    
    return n * F(n - 1)

print(F(int(si.readline().rstrip())))