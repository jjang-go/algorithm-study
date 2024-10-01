from sys import stdin as si

X = int(si.readline().rstrip())
Y = int(si.readline().rstrip())

if X > 0 and Y > 0: print(1)
elif X < 0 and Y > 0: print(2)
elif X < 0 and Y < 0: print(3)
else: print(4)