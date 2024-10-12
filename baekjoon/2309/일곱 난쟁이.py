from sys import stdin as si

arr = [0] * 9

sum = 0

for i in range(0,9):
    arr[i] = int(si.readline().rstrip())
    sum += arr[i]

arr.sort()
    
def f():
    for i in range(0, 9):
        for j in range(0,9):
            if i == j:
                continue
            
            if sum - arr[i] - arr[j] == 100:
                A = arr[i]
                B = arr[j]
                arr.remove(A)
                arr.remove(B)
                return
        
f()

for d in arr:
    print(d)