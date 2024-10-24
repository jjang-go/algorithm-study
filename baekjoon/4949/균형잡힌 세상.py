from sys import stdin as si

while True:
    arr = si.readline().rstrip()
    
    if arr[0] == '.':
        break
    
    st = []
    
    tmp = []
    
    flag = True
    
    for data in arr:
        if data == '(' or data == '[':
            tmp.append(data)
        elif data == ')':
            if tmp and tmp[-1] == '(':
                tmp.pop()
            else:
                flag = False
                break
        elif data == ']':
            if tmp and tmp[-1] == '[':
                tmp.pop()
            else:
                flag = False
                break
    
    if tmp or not flag:
        print("no")
    else:
        print("yes")