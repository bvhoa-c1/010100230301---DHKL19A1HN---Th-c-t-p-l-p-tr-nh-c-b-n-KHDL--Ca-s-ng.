def cubesum(n):
    tong = 0

    while n > 0:
        digit = n % 10
        tong += digit ** 3
        n //= 10

    return tong


n = int(input("Nhap n: "))
print("Tong lap phuong cac chu so =", cubesum(n))