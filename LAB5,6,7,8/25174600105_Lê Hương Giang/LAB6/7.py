m = int(input("Nhập số hàng: "))
n = int(input("Nhập số cột: "))
a = []
tong = 0
for i in range(m):
    hang = []
    for j in range(n):
        x = int(input("Nhập phần tử: "))
        hang.append(x)
        tong += x
    a.append(hang)
print("Tổng các phần tử trong ma trận là:", tong)