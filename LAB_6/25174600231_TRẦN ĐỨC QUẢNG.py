"""LAB6 :DANH SÁCH VÀ BỘ  """
# bài 6.1
n = int(input("Nhập số lượng phần tử: "))
a = []
for i in range(n):
    a.append(int(input(f"Nhập số thứ {i+1}: ")))

tong_chan = 0
tong_le = 0

for x in a:
    if x % 2 == 0:
        tong_chan += x # Số chẵn
    else:
        tong_le += x   # Số lẻ

print("Tổng các số chẵn:", tong_chan)
print("Tổng các số lẻ:", tong_le)

# bai 6.2 
def la_so_nguyen_to(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
def la_so_hoan_hao(n):
    tong_uoc = 0
    for i in range(1, n):
        if n % i == 0: tong_uoc += i
    return tong_uoc == n
print("Các số nguyên tố:", [x for x in a if la_so_nguyen_to(x)])
print("Các số hoàn hảo:", [x for x in a if la_so_hoan_hao(x)])

# bài 6.3 :
day_so = [3, 1.5, 10, 7.2, 0] 
print("Giá trị lớn nhất:", max(day_so))
print("Giá trị nhỏ nhất:", min(day_so))

# bai 6.4 :
n = int(input("Nhập n: "))
fibo = [0, 1]
for i in range(2, n):
    fibo.append(fibo[i-1] + fibo[i-2])

print(f"{n} số hạng đầu tiên của Fibonacci:", fibo[:n])

# bài 6.5 :
snt_100 = [x for x in range(2, 100) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))]
print("Số nguyên tố < 100:", snt_100)


# bài 6.6 :
a = [2, 4, 6, 8, 10] 
is_csc = True
khoang_cach = a[1] - a[0]

for i in range(len(a) - 1):
    if a[i+1] - a[i] != khoang_cach:
        is_csc = False
        break

if is_csc:
    print("Đây là cấp số cộng.")
else:
    print("Đây không phải cấp số cộng.")

# bài 6.7 :
ma_tran = [
    [1, 2, 3],
    [4, 5, 6]
]
tong = 0
for hang in ma_tran:
    tong += sum(hang) 
print("Tổng ma trận:", tong)

# bài 6.8 : 
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = [[0, 0], [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[i][j] += A[i][k] * B[k][j]

print("Tích hai ma trận:", C)

# bài 6.9 :
mt = [[1, 2], [2, 1]]
chuyen_vi = [[mt[j][i] for j in range(len(mt))] for i in range(len(mt[0]))]

print("Ma trận chuyển vị:", chuyen_vi)
if mt == chuyen_vi:
    print("Đây là ma trận đối xứng.")

# bài 6.10 :
print("Nhập các phần tử cho ma trận A (2x2):")
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
d = float(input("Nhập d: "))
det = a * d - b * c
if det == 0:
    print("Ma trận không khả nghịch (không có ma trận nghịch đảo).")
else:
    inv_a = d / det
    inv_b = -b / det
    inv_c = -c / det
    inv_d = a / det

    print("--- Ma trận nghịch đảo là ---")
    print(f"[{inv_a}, {inv_b}]")
    print(f"[{inv_c}, {inv_d}]")