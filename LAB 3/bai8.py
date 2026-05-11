n = int(input("Nhập n: "))

max_sum = 0
so_max = 0

for i in range(1, n + 1):
    tong = 0
    
    for j in str(i):
        tong += int(j)
    
    if tong > max_sum:
        max_sum = tong
        so_max = i

print("Số có tổng chữ số lớn nhất là:", so_max)
print("Tổng chữ số là:", max_sum)