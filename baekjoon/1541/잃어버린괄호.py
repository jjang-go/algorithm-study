from sys import stdin as si

L = si.readline().split('-')

num = []

for string in L:
    sum = 0
    sub = string.split('+')
    for n in sub:
        sum += int(n)
    num.append(sum)

for i in range(1, len(num)):
    num[0] -= num[i]

print(num[0])