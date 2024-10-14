from sys import stdin as si

while True:
    arr = list(map(str,si.readline().split()))
    
    data = arr[0]
    arr = arr[1:]
    
    if data == '#':
        break
    
    print(str(arr).lower().count(data))