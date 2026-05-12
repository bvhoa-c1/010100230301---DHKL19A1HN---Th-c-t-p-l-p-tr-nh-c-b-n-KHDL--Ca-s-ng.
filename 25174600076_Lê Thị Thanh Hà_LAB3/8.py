def tong_chu_so(n):
    tong = 0
    while n > 0:
        tong+=n%10
        n//=10
        return tong
n = int(input("Nhập n: "))
max_tong = -1
so_tim_duoc = 0

for i in range(1, n + 1):
    tong = tong_chu_so(i)
    if tong > max_tong:
        max_tong = tong
        so_tim_duoc = i
print(f"Số có tổng chữ số lớn nhất là: {so_tim_duoc} (Tổng = {max_tong})")