n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("n phải > 0, vui lòng nhập lại: "))

max_sum = -1
so_max = -1

for i in range(1, n + 1):
    tong_chu_so = sum(int(ch) for ch in str(i)) 
    if tong_chu_so > max_sum:
        max_sum = tong_chu_so
        so_max = i

print("Số có tổng chữ số lớn nhất trong khoảng [1,", n, "] là:", so_max)
print("Tổng chữ số =", max_sum)