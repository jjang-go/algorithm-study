from sys import stdin as si

N = int(si.readline().rstrip())

_dict = {}

for _ in range(N):
    Name, State = map(str, si.readline().split())
    _dict[Name] = State
    
items = sorted(_dict.items(), reverse=True)
for data in items:
    if data[1] == 'enter':
        print(data[0])