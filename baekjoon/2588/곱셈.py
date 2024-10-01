from sys import stdin as si

A = int(si.readline().rstrip())
B = int(si.readline().rstrip())

print(A * (B % 10))
print(A * (int(B / 10) % 10))
print(A * (int(B / 100) % 10))
print(A * B)