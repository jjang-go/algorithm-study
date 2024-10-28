from sys import stdin as si

def math():
    a, b, c, d, e, f = map(int, si.readline().split())

    for i in range(-999,1000):
        for j in range(-999,1000):
            if (a * i) + (b * j) == c and (d * i) + (e * j) == f:
                print(i, j)
                return

if __name__ == "__main__":
    math()