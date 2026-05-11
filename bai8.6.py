# Hàm sumPdivisors tính tổng các ước số thực sự của số nguyên dương

# Hàm tính tổng ước số thực sự
def sumPdivisors(n):
    tong = 0

    for i in range(1, n):
        if n % i == 0:
            tong += i

    return tong

# Nhập số nguyên dương
n = int(input("Nhap so nguyen duong: "))

# Xuất kết quả
print("Tong cac uoc so thuc su cua", n, "la:", sumPdivisors(n))