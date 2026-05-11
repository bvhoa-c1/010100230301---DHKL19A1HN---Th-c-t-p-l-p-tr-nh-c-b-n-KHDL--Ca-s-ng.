n = int(input("Nhập n: "))
dem = 0

for i in range(1, n + 1):
    # Chuyển i thành chuỗi, lấy từng ký tự ép về int rồi tính tổng
    tong_chu_so = sum(int(chu_so) for chu_so in str(i))
    
    if tong_chu_so % 2 == 0:
        dem += 1

print(f"Có {dem} số có tổng chữ số là số chẵn.")