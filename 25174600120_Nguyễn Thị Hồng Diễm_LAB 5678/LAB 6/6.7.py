m = int(input("Nhập hàng: "))
n = int(input("Nhập cột: "))
ma_tran = []
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input(f"Nhập phần tử [{i}][{j}]:"))
        hang.append(x)
    ma_tran.append(hang)
tong = 0
for i in range(m):
    for j in range(n):
        tong += ma_tran[i][j]
print("ma trận:")
for hang in ma_tran:
    print(hang)
print("tổng", tong)