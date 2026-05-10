n = int(input("Nhập n: "))
max_tong = 0
so_max = 0

for i in range(1, n + 1):
    tong = 0
    temp = i
    while temp > 0:
        tong += temp % 10
        temp //= 10
    if tong > max_tong:
        max_tong = tong
        so_max = i

print("Số cần tìm:", so_max)