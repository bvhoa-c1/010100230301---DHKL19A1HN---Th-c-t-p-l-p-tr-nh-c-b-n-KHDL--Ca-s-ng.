n = int(input("Nhập n: "))

max_tong = 0
so_max = 0

for i in range(1, n + 1):
    tong = sum(int(chu_so) for chu_so in str(i))
    
    if tong > max_tong:
        max_tong = tong
        so_max = i

print("Số có tổng chữ số lớn nhất là:", so_max)
print("Tổng chữ số lớn nhất là:", max_tong)