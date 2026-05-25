from math import *
def snt(n):
    if n < 2:
        return False
    for i in range(2, (isqrt(n) + 1)):
        if n % i == 0:
            return False
    return True
def doi(h):
    for i in range(2 , h + 1):
        if snt(i) and snt( i + 2):
            print(i, i + 2, end = "\n")

if __name__ == "__main__":
    doi(1000)








