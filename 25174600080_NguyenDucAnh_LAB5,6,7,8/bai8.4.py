# Hàm cubesum tính tổng lập phương các chữ số của một số

# Hàm cubesum
def cubesum(n):
    tong = 0

    while n > 0:
        chu_so = n % 10
        tong += chu_so ** 3
        n //= 10

    return tong

# Nhập số nguyên
n = int(input("Nhap mot so nguyen: "))

# Xuất kết quả
print("Tong lap phuong cac chu so la:", cubesum(n))