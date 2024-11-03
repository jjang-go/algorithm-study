from sys import stdin as si

ci = 0

def recursion(s, l, r):
    global ci
    ci += 1
    if (l >= r): 
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)
    
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)

T = int(si.readline().rstrip())

for _ in range(0,T):
    print(isPalindrome(si.readline().rstrip()), ci)
    ci = 0