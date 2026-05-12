# Bài 6.1
s = input("Nhập xâu dữ liệu: ")

# Xóa toàn bộ khoảng trắng, dấu cách, tab...
ket_qua = "".join(s.split())

print(f"Xâu sau khi loại bỏ khoảng trắng: {ket_qua}")
# Bài 6.2
s = input("Nhập xâu dữ liệu: ")

# Xóa toàn bộ khoảng trắng, dấu cách, tab...
ket_qua = "".join(s.split())

print(f"Xâu sau khi loại bỏ khoảng trắng: {ket_qua}")
# Bài 6.3
# Nhập dãy hỗn hợp trên cùng 1 dòng, cách nhau bởi dấu cách
day_nhap = input("Nhập dãy hỗn hợp (cách nhau bởi dấu cách): ").split()

# Ép kiểu toàn bộ về float để so sánh đồng nhất
day_so = [float(x) for x in day_nhap]

print(f"Giá trị lớn nhất: {max(day_so)}")
print(f"Giá trị nhỏ nhất: {min(day_so)}")
# Bài 6.4
n = int(input("Nhập số n: "))

if n <= 0:
    print("Mảng rỗng []")
elif n == 1:
    print([0])
else:
    fib = [0, 1]
    # Thủ thuật: Dùng list comprehension để duyệt và gọi lệnh append
    [fib.append(fib[-1] + fib[-2]) for _ in range(n - 2)]
    print(f"{n} số hạng đầu tiên của Fibonacci: {fib}")
# Bài 6.5
# Điều kiện: Xét mọi x từ 2->99. Chỉ lấy x nếu nó không chia hết cho bất kỳ số nào từ 2 đến căn bậc 2 của x.
primes = [x for x in range(2, 100) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]

print("Các số nguyên tố nhỏ hơn 100:")
print(primes)
# Bài 6.6
n = int(input("Nhập số lượng phần tử n (>= 2): "))
a = [float(input(f"Phần tử {i+1}: ")) for i in range(n)]

if n < 2:
    print("Cấp số cộng cần ít nhất 2 phần tử.")
else:
    # Tính công sai d dựa trên 2 phần tử đầu
    d = a[1] - a[0]
    
    # Kiểm tra xem TẤT CẢ các khoảng cách còn lại có bằng d hay không
    la_csc = all(a[i] - a[i-1] == d for i in range(1, n))
    
    if la_csc:
        print(f"Dãy LÀ cấp số cộng với công sai d = {d}")
    else:
        print("Dãy KHÔNG LÀ cấp số cộng.")
# Bài 6.7
m = int(input("Nhập số hàng m: "))
n = int(input("Nhập số cột n: "))
matrix = []

for i in range(m):
    # Dùng List comp để nhập nhanh từng hàng
    hang = [float(input(f"Nhập M[{i}][{j}]: ")) for j in range(n)]
    matrix.append(hang)

# Tính tổng: Sum của tổng từng hàng
tong = sum(sum(hang) for hang in matrix)
print(f"Tổng của toàn bộ phần tử trong ma trận là: {tong}")
# Bài 6.8
print("--- KHỞI TẠO MA TRẬN A ---")
hang_A, cot_A = int(input("Hàng A: ")), int(input("Cột A: "))
A = [[float(input(f"A[{i}][{j}]: ")) for j in range(cot_A)] for i in range(hang_A)]

print("\n--- KHỞI TẠO MA TRẬN B ---")
hang_B, cot_B = int(input("Hàng B: ")), int(input("Cột B: "))
B = [[float(input(f"B[{i}][{j}]: ")) for j in range(cot_B)] for i in range(hang_B)]

# Điều kiện nhân ma trận
if cot_A != hang_B:
    print("\nLỖI: Không thể nhân hai ma trận (Số cột A phải bằng số hàng B).")
else:
    # Thuật toán nhân ma trận O(n^3)
    C = [[sum(A[i][k] * B[k][j] for k in range(cot_A)) for j in range(cot_B)] for i in range(hang_A)]
    
    print("\nMa trận tích C = A x B:")
    for hang in C:
        print(hang)
# Bài 6.9
n = int(input("Nhập kích thước ma trận vuông n x n: "))
A = [[float(input(f"A[{i}][{j}]: ")) for j in range(n)] for i in range(n)]

# Chuyển vị: Lấy cột của A làm hàng của A_T
A_T = [[A[j][i] for j in range(n)] for i in range(n)]

print("\nMa trận gốc A:")
for hang in A: print(hang)

print("\nMa trận chuyển vị A_T:")
for hang in A_T: print(hang)

# Ma trận đối xứng khi bản gốc bằng chính bản chuyển vị của nó
if A == A_T:
    print("\n=> Đây LÀ ma trận đối xứng.")
else:
    print("\n=> Đây KHÔNG phải ma trận đối xứng.")
# Bài 6.10
n = int(input("Nhập kích thước ma trận vuông n: "))
A = [[float(input(f"A[{i}][{j}]: ")) for j in range(n)] for i in range(n)]

# Bước 1: Tạo ma trận mở rộng M = [A | I]
M = []
for i in range(n):
    # Tạo hàng của ma trận đơn vị I
    hang_I = [1.0 if i == j else 0.0 for j in range(n)]
    M.append(A[i] + hang_I)

kha_nghich = True

# Bước 2: Quá trình khử Gauss-Jordan
for i in range(n):
    # Tìm phần tử trụ (pivot) lớn nhất trong cột để tránh sai số chia cho số quá nhỏ
    pivot_row = max(range(i, n), key=lambda r: abs(M[r][i]))
    
    # Đổi chỗ hàng hiện tại với hàng có pivot lớn nhất
    M[i], M[pivot_row] = M[pivot_row], M[i]
    
    pivot = M[i][i]
    
    # Nếu phần tử trụ bằng 0, định thức bằng 0 -> Không khả nghịch
    if pivot == 0:
        kha_nghich = False
        break
        
    # Chuẩn hóa hàng i (chia cả hàng cho phần tử trụ)
    M[i] = [x / pivot for x in M[i]]
    
    # Khử các phần tử khác cùng cột i về 0
    for j in range(n):
        if i != j:
            factor = M[j][i]
            M[j] = [M[j][k] - factor * M[i][k] for k in range(2 * n)]

# Bước 3: Xuất kết quả
if kha_nghich:
    print("\nMa trận nghịch đảo A^-1:")
    for row in M:
        # Lấy nửa sau của ma trận mở rộng (từ cột n trở đi)
        nghich_dao_row = [round(x, 4) for x in row[n:]]
        print(nghich_dao_row)
else:
    print("\nMa trận này KHÔNG khả nghịch (Định thức = 0)!")

