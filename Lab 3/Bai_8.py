n = int(input("Nhập n: "))
max_tong_chu_so = -1
so_can_tim = -1
for i in range(1, n + 1):
    tong_chu_so = sum(int(digit) for digit in str(i))
    if tong_chu_so > max_tong_chu_so:
        max_tong_chu_so = tong_chu_so
        so_can_tim = i
print("Số có tổng chữ số lớn nhất:", so_can_tim)