from sys import stdin as si

while True:
    N = int(si.readline().rstrip())
    
    if N == -1:
        break
    
    d = []
    for i in range(1, N + 1):
        if N % i == 0 and N != i:
            d.append(i)

    if N == sum(d):
        print(f"{N} = {' + '.join(str(num) for num in d)}")
    else:
        print(f"{N} is NOT perfect.")
    