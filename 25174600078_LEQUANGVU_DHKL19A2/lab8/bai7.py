def sumPdivisors(n):
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i

    return tong


def isAmicable(a, b):
    return sumPdivisors(a) == b and sumPdivisors(b) == a


a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

if isAmicable(a, b):
    print("La cap so Amicable")
else:
    print("Khong phai cap so Amicable")