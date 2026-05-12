# Bài 6.1:
n = int(input("Nhấp số phần tử:"))
danh_sach = []
for i in range(n):
    so = int(input("Nhập phần tử:"))
    danh_sach.append(so)
tong_chan = 0
tong_le = 0
for so in danh_sach:
    if so % 2 == 0:
        tong_chan += so
    else:
        tong_le += so
print("Tổng số chẵn là:", tong_chan)
print("Tổng số lẻ là:", tong_le)
# BÀi 6.2
def kiem_tra_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def kiem_tra_so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
n = int(input("Nhập số phần tử:"))
danh_sach = []
for i in range(n):
    so = int(input("Nhập phần tử;"))
    danh_sach.append(so)
print("các số nguyên tố hoặc số hoàn hảo là:")
for so in danh_sach:
    if kiem_tra_so_nguyen_to(so) or kiem_tra_so_hoan_hao(so):
        print(so)
# Bai 6.3
n = int(input("Nhập số phần tử:"))
danh_sach = []
for i in range(n):
    gia_tri = float(input("Nhập ggias trị:"))
    danh_sach.append(gia_tri)
print("Giá trị lớn nhất là:", max(danh_sach))
print("Giá trị nhỏ nhất là:", min(danh_sach))
# Bài 6.4
n = int(input("Nhập n:"))
fibonacci = [0,1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for i in range(2, n)]
print("Dãy fibonacci lad:")
print(fibonacci[:n])
# Bài 6.5
danh_sach_so_nguyen_to = [
    so for so in range(2, 100)
    if all(so % i != 0 for i in range(2, int(so ** 0.5) + 1))
]
print("Các số nguyên tố nhỏ hớn 100 là:")
print(danh_sach_so_nguyen_to)
# Bài 6.6
n = int(input("Nhập số phần tử: "))
danh_sach = []
for i in range(n):

    so = int(input("Nhập phần tử: "))
    danh_sach.append(so)
cong_sai = danh_sach[1] - danh_sach[0]
la_cap_so_cong = True
for i in range(1, n - 1):
    if danh_sach[i + 1] - danh_sach[i] != cong_sai:
        la_cap_so_cong = False
        break
if la_cap_so_cong:
    print("Đây là cấp số cộng")
else:
    print("Đây không phải cấp số cộng")
# Bài 6.7
so_hang = int(input("Nhập số hàng:"))
so_cot = int(input("Nhập số cột:"))
ma_tran = []
for i in range(so_hang):
    dong = list(map(int, input("Nhập các phần tử của hàng:").split()))
    ma_tran.append(dong)
tong = 0
for dong in ma_tran:
    tong += sum(dong)
print("Tổng các phần tử trong ma trận là;", tong)
# Bài 6.8
m = int(input("Nhập số hàng của A: "))
n = int(input("Nhập số cột của A: "))
A = []
for i in range(m):
    hang = []
    for j in range(n):
        so = int(input(f"A[{i}][{j}]: "))
        hang.append(so)
    A.append(hang)
p = int(input("Nhập số hàng của B: "))
q = int(input("Nhập số cột của B: "))
B = []
for i in range(p):
    hang = []
    for j in range(q):
        so = int(input(f"B[{i}][{j}]: "))
        hang.append(so)
    B.append(hang)
if n != p:
    print("Không thể nhân hai ma trận")
else:
    ket_qua = []
    for i in range(m):
        hang = []
        for j in range(q):
            tong = 0
            for k in range(n):
                tong += A[i][k] * B[k][j]
            hang.append(tong)
        ket_qua.append(hang)
    print("Ma trận tích:")
    for hang in ket_qua:
        print(hang)
# Bài 6.9
n = int(input("Nhập kích thước ma trận vuông: "))
ma_tran = []
for i in range(n):
    hang = []
    for j in range(n):
        so = int(input(f"Phần tử [{i}][{j}]: "))
        hang.append(so)
    ma_tran.append(hang)
chuyen_vi = []
for j in range(n):
    hang = []
    for i in range(n):
        hang.append(ma_tran[i][j])
    chuyen_vi.append(hang)
print("Ma trận chuyển vị:")
for hang in chuyen_vi:
    print(hang)
if ma_tran == chuyen_vi:
    print("Đây là ma trận đối xứng")
else:
    print("Đây không phải ma trận đối xứng")
# Bài 6.10
import numpy as np
n = int(input("Nhập kích thước ma trận vuông: "))
ma_tran = []
for i in range(n):
    hang = []
    for j in range(n):
        so = float(input(f"Nhập phần tử [{i}][{j}]: "))
        hang.append(so)
    ma_tran.append(hang)
A = np.array(ma_tran)
dinh_thuc = np.linalg.det(A)
if dinh_thuc == 0:
    print("Ma trận không có nghịch đảo")
else:
    nghich_dao = np.linalg.inv(A)
    print("Ma trận nghịch đảo là:")
    print(nghich_dao)