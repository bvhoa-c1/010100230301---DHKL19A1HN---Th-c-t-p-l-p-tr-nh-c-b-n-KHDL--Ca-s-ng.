n = int(input("Nhập số n: "))
so = 1
S = 1

for i in range(1,n+1):
    tong = 0
    for j in str(i):
        tong += int(j)
    # tổng mới lớn hơn tổng cũ
    if tong > S :
        S = tong
        so = i
print("Số có tổng chữ số lớn nhất là: ",so)