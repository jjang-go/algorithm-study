from sys import stdin as si
st = []

T = int(si.readline().rstrip())

while T >= 1:
    T -= 1
    num  = int(si.readline().rstrip())
    
    if num == 0:
        st.pop()
    else:
        st.append(num)
print(sum(st))
