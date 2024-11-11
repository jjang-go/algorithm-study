from sys import stdin as si

sum = 0

for _ in range(5):
    tmp = int(si.readline().rstrip())
    if tmp < 40:
        sum += 40
    else:
        sum += tmp
    
print(int(sum / 5))