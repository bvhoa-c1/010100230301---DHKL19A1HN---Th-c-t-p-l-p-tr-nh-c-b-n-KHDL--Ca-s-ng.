# Kiểm tra số Armstrong bằng cách sử dụng hàm cubesum

# Hàm tính tổng lập phương các chữ số
def cubesum(n):
    tong = 0
    tam = n

    while tam > 0:
        chu_so = tam % 10
        tong += chu_so ** 3
        tam //= 10

    return tong

# Hàm kiểm tra số Armstrong
def la_so_armstrong(n):
    return n == cubesum(n)

# Nhập số cần kiểm tra
n = int(input("Nhap mot so nguyen: "))

# Kiểm tra và xuất kết quả
if la_so_armstrong(n):
    print(n, "la so Armstrong")
else:
    print(n, "khong phai la so Armstrong")

# Xuất danh sách số Armstrong nhỏ hơn 1000
print("\nCac so Armstrong nho hon 1000:")

for i in range(1000):
    if la_so_armstrong(i):
        print(i, end=" ")