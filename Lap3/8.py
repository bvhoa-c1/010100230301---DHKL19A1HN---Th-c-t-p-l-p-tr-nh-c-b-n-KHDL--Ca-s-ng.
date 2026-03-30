n = int(input("Nhập n: "))
max_sum = 0
so = 0
for i in range(1, n + 1):
    tong = sum(int(d) for d in str(i))
    if tong > max_sum:
        max_sum = tong
        so = i
print("Số cần tìm:", so)
print("Tổng chữ số lớn nhất:", max_sum)