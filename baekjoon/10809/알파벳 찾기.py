from sys import stdin as si

List = [-1] * 26

word = si.readline().strip()

for i in range(0,len(word)):
    if List[ord(word[i])-ord('a')] == -1:
        List[ord(word[i])-ord('a')] = i

for d in List:
    print(d, end=" ")