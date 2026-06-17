#Bài 6.1:
n = int(input("Nhập số lượng phần tử: "))
danh_sach = []
for i in range(n):
    so = int(input("Nhập số: "))
    danh_sach.append(so)
tong_chan = 0
tong_le = 0
for so in danh_sach:
    if so % 2 == 0:
        tong_chan += so
    else:
        tong_le += so
print("Tổng số chẵn:", tong_chan)
print("Tổng số lẻ:", tong_le)

#Bài 6.2:
def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def la_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n
n = int(input("Nhập số lượng phần tử: "))
danh_sach = []
for i in range(n):
    so = int(input("Nhập số: "))
    danh_sach.append(so)
print("Các số nguyên tố")
for so in danh_sach:
    if la_so_nguyen_to(so):
        print(so)
print("các số hoàn hảo: ")
for so in danh_sach:
    if la_hoan_hao(so):
        print(so)

#Bài 6.3:
n =int(input("Nhập số lượn phần tử: "))
danh_sach = []
for i in range(n):
    so = float(input("Nhập số: "))
    danh_sach.append(so)
lon_nhat = max(danh_sach)
nho_nhat = min(danh_sach)
print("Giá trị lớn nhất: ", lon_nhat)
print("Giá trị nhỏ nhất: ", nho_nhat)

#Bài 6.4:
n = int(input("Nhập số lượng số fibonacci: "))
fibonacci = [0,1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2])
 for i in range(2, n)]
print("Dãy fibonacci: ")
print(fibonacci[:n])

#Bài 6.5:
def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
danh_sach = [so for so in range(100) if la_nguyen_to(so)]
print("các số nguyên tố nhỏ hơn 100: ")
print(danh_sach)

#BÀi 6.6:
n = int(input("Nhập số lượng phần tử: "))
danh_sach = []
for i in range(n):
    so = int(input("Nhập só: "))
    danh_sach.append(so)
cong_sai = danh_sach[1] - danh_sach[0]
la_cap_so_cong = True
for i in range(1, n-1):
    if danh_sach[i+1] - danh_sach[i] != cong_sai:
        la_cap_so_cong = False
        break
if la_cap_so_cong:
    print("Đây là cấp số cộng")
else:
    print("Đây không phải là cấp số cọng")

#Bài 6.7:
m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
ma_tran = []
for i in range(m):
    hang = []
    for j in range(n):
        so = int(input(f"NHập phần tử [{i}][{j}]: "))
        hang.append(so)
    ma_tran.append(hang)
tong = 0
for hang in ma_tran:
    tong += sum(hang)
print("Tổng các phần tử: ", tong)

#Bài 6.8:
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

#BÀi 6.9:
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

#Bài 6.10:
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
