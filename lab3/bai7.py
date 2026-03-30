n = int(input("Nhập n: "))

dem = 0

for i in range(1, n + 1):
    tong = sum(int(chu_so) for chu_so in str(i))
    if tong % 2 == 0:
        dem += 1

print("Số lượng số có tổng chữ số chẵn là:", dem)