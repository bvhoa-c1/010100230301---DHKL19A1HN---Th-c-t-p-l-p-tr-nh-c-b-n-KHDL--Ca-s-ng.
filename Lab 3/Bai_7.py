n = int(input("Nhập n: "))
dem = 0
for i in range(1, n + 1):
    tong_chu_so = sum(int(digit) for digit in str(i))
    if tong_chu_so % 2 == 0:
        dem += 1
print("Số lượng số có tổng chữ số chẵn:", dem)