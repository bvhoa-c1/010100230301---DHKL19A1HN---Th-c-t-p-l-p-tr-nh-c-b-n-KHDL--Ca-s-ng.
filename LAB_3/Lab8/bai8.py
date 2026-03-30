n = int(input("Nhập n: "))
max_sum = 0
number = 0
for i in range(1, n + 1):
    s = 0
    temp = i
    while temp > 0:
        s += temp % 10
        temp //= 10
    if s > max_sum:
        max_sum = s
        number = i
print("Số có tổng chữ số lớn nhất:", number)
print("Tổng chữ số:", max_sum)