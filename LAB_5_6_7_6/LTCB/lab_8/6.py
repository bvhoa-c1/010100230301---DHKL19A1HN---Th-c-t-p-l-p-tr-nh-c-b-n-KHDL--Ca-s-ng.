n = int(input())
def sumPdivisors(n):
    tong = 0
    for i in range(1, n +1):
        if n % i == 0:
            tong += i
    return tong
print(sumPdivisors(n))