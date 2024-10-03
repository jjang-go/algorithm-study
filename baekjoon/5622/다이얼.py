from sys import stdin as si

s = si.readline().strip()

sum = 0

for w in s:
    if w == 'A' or w == 'B' or w == 'C':
        sum += 3
    elif w == 'D' or w == 'E' or w == 'F':
        sum += 4
    elif w == 'G' or w == 'H' or w == 'I':
        sum += 5
    elif w == 'J' or w == 'K' or w == 'L':
        sum += 6
    elif w == 'M' or w == 'N' or w == 'O':
        sum += 7
    elif w == 'P' or w == 'Q' or w == 'R' or w == 'S':
        sum += 8
    elif w == 'T' or w == 'U' or w == 'V':
        sum += 9
    else:
        sum += 10

print(sum)