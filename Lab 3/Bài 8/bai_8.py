n = int(input("Nhập n: "))

def tong_cs(x):
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s

max_sum = -1
so = 0

for i in range(1, n+1):
    if tong_cs(i) > max_sum:
        max_sum = tong_cs(i)
        so = i

print("Số có tổng chữ số lớn nhất:", so)