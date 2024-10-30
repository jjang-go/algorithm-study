from sys import stdin as si

line = si.readline().rstrip()

line = sorted(line,reverse=True)

for l in line:
    print(l,end="")