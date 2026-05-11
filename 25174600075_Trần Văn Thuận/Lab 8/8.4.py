def cubesum(n):
    tong = 0
    while n > 0:
        so = n % 10
        tong += so**3
        n //= 10
    return tong
n = int(input("Nhập số: "))
print("tổng lập phương các chữ số:", cubesum(n))