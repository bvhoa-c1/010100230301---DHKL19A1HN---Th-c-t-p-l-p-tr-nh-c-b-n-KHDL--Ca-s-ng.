n = int(input("Nhập n: "))
max_tong = 0
so_max_tong = 0

for i in range(1, n + 1):
    tong = sum(int(chu_so) for chu_so in str(i))
    if tong > max_tong:
        max_tong = tong
        so_max_tong = i
        
print(f"Số có tổng chữ số lớn nhất là {so_max_tong} (Tổng = {max_tong})")