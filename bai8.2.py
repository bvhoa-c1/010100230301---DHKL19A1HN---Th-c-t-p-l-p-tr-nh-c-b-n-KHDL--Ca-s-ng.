# Xây dựng hàm tính giai thừa của một số nguyên dương

# Hàm tính giai thừa
def giai_thua(n):
    ket_qua = 1

    for i in range(1, n + 1):
        ket_qua *= i

    return ket_qua

# Nhập dữ liệu
n = int(input("Nhap so nguyen duong: "))

# Xuất kết quả
print("Giai thua cua", n, "la:", giai_thua(n))