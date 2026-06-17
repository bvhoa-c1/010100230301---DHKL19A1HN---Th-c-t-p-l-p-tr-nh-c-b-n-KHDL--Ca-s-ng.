# Bài 8.3
# Xây dựng hàm tính giai thừa, hoán vị và tổ hợp

# Hàm tính giai thừa
def giai_thua(n):
    ket_qua = 1

    for i in range(1, n + 1):
        ket_qua *= i

    return ket_qua

# Hàm tính hoán vị
def hoan_vi(n, r):
    return giai_thua(n) // giai_thua(n - r)

# Hàm tính tổ hợp
def to_hop(n, r):
    return giai_thua(n) // (giai_thua(r) * giai_thua(n - r))

# Nhập dữ liệu
n = int(input("Nhap n: "))
r = int(input("Nhap r: "))

# Xuất kết quả
print("Hoan vi P(n, r) =", hoan_vi(n, r))
print("To hop C(n, r) =", to_hop(n, r))