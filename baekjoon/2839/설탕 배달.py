from sys import stdin as si

N = int(si.readline().rstrip())

cnt = 0

if N % 5 == 0:
    cnt = N // 5
else:
    while N > 0:
        # N에서 3을 뺀 뒤 카운트를 추가한다.
        N -= 3
        cnt += 1
        
        if N % 5 == 0:
            cnt += N // 5
            break
        elif N == 1 or N == 2:
            cnt = -1
            break
        elif N == 0:
            break
        
print(cnt)