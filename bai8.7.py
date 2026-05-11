# Hàm tính tổng các ước số thực sự của n
def sumDivisors(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong

# Hàm kiểm tra cặp số Amicable
def isAmicable(a, b):
    return sumDivisors(a) == b and sumDivisors(b) == a

# Nhập dữ liệu
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))

# Kiểm tra
if isAmicable(a, b):
    print(a, "và", b, "là cặp số Amicable")
else:
    print(a, "và", b, "không phải cặp số Amicable")