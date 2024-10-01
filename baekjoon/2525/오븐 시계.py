from sys import stdin as si

H, M = map(int,si.readline().split())

AM = int(si.readline().rstrip())

print("{0} {1}".format((H + int((M + AM)/60)) % 24,(M + AM) % 60))