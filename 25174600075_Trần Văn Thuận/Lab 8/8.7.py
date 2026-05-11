def sumpdivisors(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong
def amicable(a, b):
    if sumpdivisors(a) == b and sumpdivisors(b) == a:
        return True
    return False
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if amicable(a, b):
    print("Đây là cặp số amicable")
else:
    print("Không phải cặp số amicable")