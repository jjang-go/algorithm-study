from sys import stdin as si

List = [0] * 1001

for _ in range(0,10):
    List[int(si.readline().rstrip())%42] += 1
    
sum = 0
for i in range(0,len(List)):
    if List[i] != 0:
        sum += 1
        
print(sum)