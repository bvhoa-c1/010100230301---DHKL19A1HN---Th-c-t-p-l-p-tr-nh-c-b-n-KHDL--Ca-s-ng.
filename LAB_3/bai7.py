n = int(input("Nhập n: "))
dem = 0

for i in range(1, n + 1):
    tong_chu_so = 0
    for chu_so in str(i):
        tong_chu_so += int(chu_so)
    

    if tong_chu_so % 2 == 0:
        dem += 1

print(f"Số lượng các số trong khoảng [1, {n}] có tổng chữ số chẵn là: {dem}")